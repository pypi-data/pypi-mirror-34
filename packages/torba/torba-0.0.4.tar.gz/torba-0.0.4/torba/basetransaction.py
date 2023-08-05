import six
import logging
from typing import List, Iterable
from binascii import hexlify

from twisted.internet import defer

import torba.baseaccount
import torba.baseledger
from torba.basescript import BaseInputScript, BaseOutputScript
from torba.coinselection import CoinSelector
from torba.constants import COIN, NULL_HASH32
from torba.bcd_data_stream import BCDataStream
from torba.hash import sha256, TXRef, TXRefImmutable, TXORef
from torba.util import ReadOnlyList


log = logging.getLogger()


class TXRefMutable(TXRef):

    __slots__ = 'tx',

    def __init__(self, tx):
        super(TXRefMutable, self).__init__()
        self.tx = tx

    @property
    def id(self):
        if self._id is None:
            self._id = hexlify(self.hash[::-1]).decode()
        return self._id

    @property
    def hash(self):
        if self._hash is None:
            self._hash = sha256(sha256(self.tx.raw))
        return self._hash

    def reset(self):
        self._id = None
        self._hash = None


class TXORefResolvable(TXORef):

    __slots__ = '_txo',

    def __init__(self, txo):
        super(TXORefResolvable, self).__init__(txo.tx_ref, txo.position)
        self._txo = txo

    @property
    def txo(self):
        return self._txo


class InputOutput(object):

    __slots__ = 'tx_ref', 'position'

    def __init__(self, tx_ref=None, position=None):
        self.tx_ref = tx_ref  # type: TXRef
        self.position = position  # type: int

    @property
    def size(self):
        """ Size of this input / output in bytes. """
        stream = BCDataStream()
        self.serialize_to(stream)
        return len(stream.get_bytes())

    def serialize_to(self, stream):
        raise NotImplemented


class BaseInput(InputOutput):

    script_class = BaseInputScript

    NULL_SIGNATURE = b'\x00'*72
    NULL_PUBLIC_KEY = b'\x00'*33

    __slots__ = 'txo_ref', 'sequence', 'coinbase', 'script'

    def __init__(self, txo_ref, script, sequence=0xFFFFFFFF, tx_ref=None, position=None):
        # type: (TXORef, BaseInputScript, int, TXRef, int) -> None
        super(BaseInput, self).__init__(tx_ref, position)
        self.txo_ref = txo_ref
        self.sequence = sequence
        self.coinbase = script if txo_ref.is_null else None
        self.script = script if not txo_ref.is_null else None  # type: BaseInputScript

    @property
    def is_coinbase(self):
        return self.coinbase is not None

    @classmethod
    def spend(cls, txo):  # type: (BaseOutput) -> BaseInput
        """ Create an input to spend the output."""
        assert txo.script.is_pay_pubkey_hash, 'Attempting to spend unsupported output.'
        script = cls.script_class.redeem_pubkey_hash(cls.NULL_SIGNATURE, cls.NULL_PUBLIC_KEY)
        return cls(txo.ref, script)

    @property
    def amount(self):
        """ Amount this input adds to the transaction. """
        if self.txo_ref.txo is None:
            raise ValueError('Cannot resolve output to get amount.')
        return self.txo_ref.txo.amount

    @classmethod
    def deserialize_from(cls, stream):
        tx_ref = TXRefImmutable.from_hash(stream.read(32))
        position = stream.read_uint32()
        script = stream.read_string()
        sequence = stream.read_uint32()
        return cls(
            TXORef(tx_ref, position),
            cls.script_class(script) if not tx_ref.is_null else script,
            sequence
        )

    def serialize_to(self, stream, alternate_script=None):
        stream.write(self.txo_ref.tx_ref.hash)
        stream.write_uint32(self.txo_ref.position)
        if alternate_script is not None:
            stream.write_string(alternate_script)
        else:
            if self.is_coinbase:
                stream.write_string(self.coinbase)
            else:
                stream.write_string(self.script.source)
        stream.write_uint32(self.sequence)


class BaseOutputEffectiveAmountEstimator(object):

    __slots__ = 'txo', 'txi', 'fee', 'effective_amount'

    def __init__(self, ledger, txo):  # type: (torba.baseledger.BaseLedger, BaseOutput) -> None
        self.txo = txo
        self.txi = ledger.transaction_class.input_class.spend(txo)
        self.fee = ledger.get_input_output_fee(self.txi)
        self.effective_amount = txo.amount - self.fee

    def __lt__(self, other):
        return self.effective_amount < other.effective_amount


class BaseOutput(InputOutput):

    script_class = BaseOutputScript
    estimator_class = BaseOutputEffectiveAmountEstimator

    __slots__ = 'amount', 'script'

    def __init__(self, amount, script, tx_ref=None, position=None):
        # type: (int, BaseOutputScript, TXRef, int) -> None
        super(BaseOutput, self).__init__(tx_ref, position)
        self.amount = amount
        self.script = script

    @property
    def ref(self):
        return TXORefResolvable(self)

    @property
    def id(self):
        return self.ref.id

    def get_estimator(self, ledger):
        return self.estimator_class(ledger, self)

    @classmethod
    def pay_pubkey_hash(cls, amount, pubkey_hash):
        return cls(amount, cls.script_class.pay_pubkey_hash(pubkey_hash))

    @classmethod
    def deserialize_from(cls, stream):
        return cls(
            amount=stream.read_uint64(),
            script=cls.script_class(stream.read_string())
        )

    def serialize_to(self, stream):
        stream.write_uint64(self.amount)
        stream.write_string(self.script.source)


class BaseTransaction:

    input_class = BaseInput
    output_class = BaseOutput

    def __init__(self, raw=None, version=1, locktime=0):
        self._raw = raw
        self.ref = TXRefMutable(self)
        self.version = version  # type: int
        self.locktime = locktime  # type: int
        self._inputs = []  # type: List[BaseInput]
        self._outputs = []  # type: List[BaseOutput]
        if raw is not None:
            self._deserialize()

    @property
    def id(self):
        return self.ref.id

    @property
    def hash(self):
        return self.ref.hash

    @property
    def raw(self):
        if self._raw is None:
            self._raw = self._serialize()
        return self._raw

    def _reset(self):
        self._raw = None
        self.ref.reset()

    @property
    def inputs(self):  # type: () -> ReadOnlyList[BaseInput]
        return ReadOnlyList(self._inputs)

    @property
    def outputs(self):  # type: () -> ReadOnlyList[BaseOutput]
        return ReadOnlyList(self._outputs)

    def _add(self, new_ios, existing_ios):
        # type: (List[InputOutput], List[InputOutput]) -> BaseTransaction
        for txio in new_ios:
            txio.tx_ref = self.ref
            txio.position = len(existing_ios)
            existing_ios.append(txio)
        self._reset()
        return self

    def add_inputs(self, inputs):  # type: (List[BaseInput]) -> BaseTransaction
        return self._add(inputs, self._inputs)

    def add_outputs(self, outputs):  # type: (List[BaseOutput]) -> BaseTransaction
        return self._add(outputs, self._outputs)

    @property
    def fee(self):  # type: () -> int
        """ Fee that will actually be paid."""
        return self.input_sum - self.output_sum

    @property
    def size(self):  # type: () -> int
        """ Size in bytes of the entire transaction. """
        return len(self.raw)

    @property
    def base_size(self):  # type: () -> int
        """ Size in bytes of transaction meta data and all outputs; without inputs. """
        return len(self._serialize(with_inputs=False))

    def _serialize(self, with_inputs=True):  # type: (bool) -> bytes
        stream = BCDataStream()
        stream.write_uint32(self.version)
        if with_inputs:
            stream.write_compact_size(len(self._inputs))
            for txin in self._inputs:
                txin.serialize_to(stream)
        stream.write_compact_size(len(self._outputs))
        for txout in self._outputs:
            txout.serialize_to(stream)
        stream.write_uint32(self.locktime)
        return stream.get_bytes()

    def _serialize_for_signature(self, signing_input):  # type: (int) -> bytes
        stream = BCDataStream()
        stream.write_uint32(self.version)
        stream.write_compact_size(len(self._inputs))
        for i, txin in enumerate(self._inputs):
            if signing_input == i:
                txin.serialize_to(stream, txin.txo_ref.txo.script.source)
            else:
                txin.serialize_to(stream, b'')
        stream.write_compact_size(len(self._outputs))
        for txout in self._outputs:
            txout.serialize_to(stream)
        stream.write_uint32(self.locktime)
        stream.write_uint32(self.signature_hash_type(1))  # signature hash type: SIGHASH_ALL
        return stream.get_bytes()

    def _deserialize(self):
        if self._raw is not None:
            stream = BCDataStream(self._raw)
            self.version = stream.read_uint32()
            input_count = stream.read_compact_size()
            self.add_inputs([
                self.input_class.deserialize_from(stream) for _ in range(input_count)
            ])
            output_count = stream.read_compact_size()
            self.add_outputs([
                self.output_class.deserialize_from(stream) for _ in range(output_count)
            ])
            self.locktime = stream.read_uint32()

    @classmethod
    def ensure_all_have_same_ledger(cls, funding_accounts, change_account=None):
        # type: (Iterable[torba.baseaccount.BaseAccount], torba.baseaccount.BaseAccount) -> torba.baseledger.BaseLedger
        ledger = None
        for account in funding_accounts:
            if ledger is None:
                ledger = account.ledger
            if ledger != account.ledger:
                raise ValueError(
                    'All funding accounts used to create a transaction must be on the same ledger.'
                )
        if change_account is not None and change_account.ledger != ledger:
            raise ValueError('Change account must use same ledger as funding accounts.')
        return ledger

    @classmethod
    @defer.inlineCallbacks
    def pay(cls, outputs, funding_accounts, change_account, reserve_outputs=True):
        # type: (List[BaseOutput], List[torba.baseaccount.BaseAccount], torba.baseaccount.BaseAccount) -> defer.Deferred
        """ Efficiently spend utxos from funding_accounts to cover the new outputs. """

        tx = cls().add_outputs(outputs)
        ledger = cls.ensure_all_have_same_ledger(funding_accounts, change_account)
        amount = tx.output_sum + ledger.get_transaction_base_fee(tx)
        txos = yield ledger.get_effective_amount_estimators(funding_accounts)
        selector = CoinSelector(
            txos, amount,
            ledger.get_input_output_fee(
                cls.output_class.pay_pubkey_hash(COIN, NULL_HASH32)
            )
        )

        spendables = selector.select()
        if not spendables:
            raise ValueError('Not enough funds to cover this transaction.')

        reserved_outputs = [s.txo.id for s in spendables]
        if reserve_outputs:
            yield ledger.db.reserve_spent_outputs(reserved_outputs)

        try:
            spent_sum = sum(s.effective_amount for s in spendables)
            if spent_sum > amount:
                change_address = yield change_account.change.get_or_create_usable_address()
                change_hash160 = change_account.ledger.address_to_hash160(change_address)
                change_amount = spent_sum - amount
                tx.add_outputs([cls.output_class.pay_pubkey_hash(change_amount, change_hash160)])

            tx.add_inputs([s.txi for s in spendables])
            yield tx.sign(funding_accounts)

        except Exception:
            if reserve_outputs:
                yield ledger.db.release_reserved_outputs(reserved_outputs)
            raise

        defer.returnValue(tx)

    @classmethod
    @defer.inlineCallbacks
    def liquidate(cls, assets, funding_accounts, change_account, reserve_outputs=True):
        """ Spend assets (utxos) supplementing with funding_accounts if fee is higher than asset value. """

        tx = cls().add_inputs([
            cls.input_class.spend(utxo) for utxo in assets
        ])
        ledger = cls.ensure_all_have_same_ledger(funding_accounts, change_account)

        reserved_outputs = [utxo.id for utxo in assets]
        if reserve_outputs:
            yield ledger.db.reserve_spent_outputs(reserved_outputs)

        try:
            cost_of_change = (
                ledger.get_transaction_base_fee(tx) +
                ledger.get_input_output_fee(cls.output_class.pay_pubkey_hash(COIN, NULL_HASH32))
            )
            liquidated_total = sum(utxo.amount for utxo in assets)
            if liquidated_total > cost_of_change:
                change_address = yield change_account.change.get_or_create_usable_address()
                change_hash160 = change_account.ledger.address_to_hash160(change_address)
                change_amount = liquidated_total - cost_of_change
                tx.add_outputs([cls.output_class.pay_pubkey_hash(change_amount, change_hash160)])

            yield tx.sign(funding_accounts)

        except Exception:
            if reserve_outputs:
                yield ledger.db.release_reserved_outputs(reserved_outputs)
            raise

        defer.returnValue(tx)

    def signature_hash_type(self, hash_type):
        return hash_type

    @defer.inlineCallbacks
    def sign(self, funding_accounts):  # type: (Iterable[torba.baseaccount.BaseAccount]) -> BaseTransaction
        ledger = self.ensure_all_have_same_ledger(funding_accounts)
        for i, txi in enumerate(self._inputs):
            txo_script = txi.txo_ref.txo.script
            if txo_script.is_pay_pubkey_hash:
                address = ledger.hash160_to_address(txo_script.values['pubkey_hash'])
                private_key = yield ledger.get_private_key_for_address(address)
                tx = self._serialize_for_signature(i)
                txi.script.values['signature'] = \
                    private_key.sign(tx) + six.int2byte(self.signature_hash_type(1))
                txi.script.values['pubkey'] = private_key.public_key.pubkey_bytes
                txi.script.generate()
            else:
                raise NotImplementedError("Don't know how to spend this output.")
        self._reset()

    def sort(self):
        # See https://github.com/kristovatlas/rfc/blob/master/bips/bip-li01.mediawiki
        self._inputs.sort(key=lambda i: (i['prevout_hash'], i['prevout_n']))
        self._outputs.sort(key=lambda o: (o[2], pay_script(o[0], o[1])))

    @property
    def input_sum(self):
        return sum(i.amount for i in self.inputs)

    @property
    def output_sum(self):
        return sum(o.amount for o in self.outputs)

    @defer.inlineCallbacks
    def get_my_addresses(self, ledger):
        addresses = set()
        for txo in self.outputs:
            address = ledger.hash160_to_address(txo.script.values['pubkey_hash'])
            record = yield ledger.db.get_address(address)
            if record is not None:
                addresses.add(address)
        defer.returnValue(list(addresses))
