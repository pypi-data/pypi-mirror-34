from binascii import hexlify, unhexlify
from twisted.trial import unittest
from twisted.internet import defer

from torba.coin.bitcoinsegwit import MainNetLedger as ledger_class
from torba.constants import CENT, COIN


NULL_HASH = b'\x00'*32
FEE_PER_BYTE = 50
FEE_PER_CHAR = 200000


def get_output(amount=CENT, pubkey_hash=NULL_HASH):
    return ledger_class.transaction_class() \
        .add_outputs([ledger_class.transaction_class.output_class.pay_pubkey_hash(amount, pubkey_hash)]) \
        .outputs[0]


def get_input():
    return ledger_class.transaction_class.input_class.spend(get_output())


def get_transaction(txo=None):
    return ledger_class.transaction_class() \
        .add_inputs([get_input()]) \
        .add_outputs([txo or ledger_class.transaction_class.output_class.pay_pubkey_hash(CENT, NULL_HASH)])


class TestSizeAndFeeEstimation(unittest.TestCase):

    def setUp(self):
        self.ledger = ledger_class({'db': ledger_class.database_class(':memory:')})
        return self.ledger.db.start()

    def io_fee(self, io):
        return self.ledger.get_input_output_fee(io)

    def test_output_size_and_fee(self):
        txo = get_output()
        self.assertEqual(txo.size, 46)
        self.assertEqual(self.io_fee(txo), 46 * FEE_PER_BYTE)

    def test_input_size_and_fee(self):
        txi = get_input()
        self.assertEqual(txi.size, 148)
        self.assertEqual(self.io_fee(txi), 148 * FEE_PER_BYTE)

    def test_transaction_size_and_fee(self):
        tx = get_transaction()
        base_size = tx.size - 1 - tx.inputs[0].size
        self.assertEqual(tx.size, 204)
        self.assertEqual(tx.base_size, base_size)
        self.assertEqual(self.ledger.get_transaction_base_fee(tx), FEE_PER_BYTE * base_size)


class TestTransactionSerialization(unittest.TestCase):

    def test_genesis_transaction(self):
        raw = unhexlify(
            '01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04'
            'ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e20'
            '6272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01'
            '000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4c'
            'ef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000'
        )
        tx = ledger_class.transaction_class(raw)
        self.assertEqual(tx.version, 1)
        self.assertEqual(tx.locktime, 0)
        self.assertEqual(len(tx.inputs), 1)
        self.assertEqual(len(tx.outputs), 1)

        coinbase = tx.inputs[0]
        self.assertTrue(coinbase.txo_ref.is_null, NULL_HASH)
        self.assertEqual(coinbase.txo_ref.position, 0xFFFFFFFF)
        self.assertEqual(coinbase.sequence, 4294967295)
        self.assertIsNotNone(coinbase.coinbase)
        self.assertIsNone(coinbase.script)
        self.assertEqual(
            coinbase.coinbase[8:],
            b'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks'
        )

        out = tx.outputs[0]
        self.assertEqual(out.amount, 5000000000)
        self.assertEqual(out.position, 0)
        self.assertTrue(out.script.is_pay_pubkey)
        self.assertFalse(out.script.is_pay_pubkey_hash)
        self.assertFalse(out.script.is_pay_script_hash)

        tx._reset()
        self.assertEqual(tx.raw, raw)

    def test_coinbase_transaction(self):
        raw = unhexlify(
            '01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4e03'
            '1f5a070473319e592f4254432e434f4d2f4e59412ffabe6d6dcceb2a9d0444c51cabc4ee97a1a000036ca0'
            'cb48d25b94b78c8367d8b868454b0100000000000000c0309b21000008c5f8f80000ffffffff0291920b5d'
            '0000000017a914e083685a1097ce1ea9e91987ab9e94eae33d8a13870000000000000000266a24aa21a9ed'
            'e6c99265a6b9e1d36c962fda0516b35709c49dc3b8176fa7e5d5f1f6197884b400000000'
        )
        tx = ledger_class.transaction_class(raw)
        self.assertEqual(tx.version, 1)
        self.assertEqual(tx.locktime, 0)
        self.assertEqual(len(tx.inputs), 1)
        self.assertEqual(len(tx.outputs), 2)

        coinbase = tx.inputs[0]
        self.assertTrue(coinbase.txo_ref.is_null)
        self.assertEqual(coinbase.txo_ref.position, 0xFFFFFFFF)
        self.assertEqual(coinbase.sequence, 4294967295)
        self.assertIsNotNone(coinbase.coinbase)
        self.assertIsNone(coinbase.script)
        self.assertEqual(coinbase.coinbase[9:22], b'/BTC.COM/NYA/')

        out = tx.outputs[0]
        self.assertEqual(out.amount, 1561039505)
        self.assertEqual(out.position, 0)
        self.assertFalse(out.script.is_pay_pubkey)
        self.assertFalse(out.script.is_pay_pubkey_hash)
        self.assertTrue(out.script.is_pay_script_hash)
        self.assertFalse(out.script.is_return_data)

        out1 = tx.outputs[1]
        self.assertEqual(out1.amount, 0)
        self.assertEqual(out1.position, 1)
        self.assertEqual(
            hexlify(out1.script.values['data']),
            b'aa21a9ede6c99265a6b9e1d36c962fda0516b35709c49dc3b8176fa7e5d5f1f6197884b4'
        )
        self.assertTrue(out1.script.is_return_data)
        self.assertFalse(out1.script.is_pay_pubkey)
        self.assertFalse(out1.script.is_pay_pubkey_hash)
        self.assertFalse(out1.script.is_pay_script_hash)

        tx._reset()
        self.assertEqual(tx.raw, raw)


class TestTransactionSigning(unittest.TestCase):

    def setUp(self):
        self.ledger = ledger_class({'db': ledger_class.database_class(':memory:')})
        return self.ledger.db.start()

    @defer.inlineCallbacks
    def test_sign(self):
        account = self.ledger.account_class.from_seed(
            self.ledger,
            u"carbon smart garage balance margin twelve chest sword toast envelope bottom stomach ab"
            u"sent", u"torba"
        )

        yield account.ensure_address_gap()
        address1, address2 = yield account.receiving.get_addresses(2)
        pubkey_hash1 = self.ledger.address_to_hash160(address1)
        pubkey_hash2 = self.ledger.address_to_hash160(address2)

        tx_class = ledger_class.transaction_class

        tx = tx_class() \
            .add_inputs([tx_class.input_class.spend(get_output(2*COIN, pubkey_hash1))]) \
            .add_outputs([tx_class.output_class.pay_pubkey_hash(int(1.9*COIN), pubkey_hash2)]) \

        yield tx.sign([account])

        self.assertEqual(
            hexlify(tx.inputs[0].script.values['signature']),
            b'304402203d463519290d06891e461ea5256c56097ccdad53379b1bb4e51ec5abc6e9fd02022034ed15b9'
            b'd7c678716c4aa7c0fd26c688e8f9db8075838f2839ab55d551b62c0a01'
        )
