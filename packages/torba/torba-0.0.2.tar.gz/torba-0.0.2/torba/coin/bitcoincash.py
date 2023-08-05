__node_daemon__ = 'bitcoind'
__node_cli__ = 'bitcoin-cli'
__node_bin__ = 'bitcoin-abc-0.17.2/bin'
__node_url__ = (
    'https://download.bitcoinabc.org/0.17.2/linux/bitcoin-abc-0.17.2-x86_64-linux-gnu.tar.gz'
)
__electrumx__ = 'electrumx.lib.coins.BitcoinCashRegtest'

from six import int2byte
from binascii import unhexlify
from torba.baseledger import BaseLedger
from torba.baseheader import BaseHeaders
from torba.basetransaction import BaseTransaction


class Transaction(BaseTransaction):

    def signature_hash_type(self, hash_type):
        return hash_type | 0x40


class MainNetLedger(BaseLedger):
    name = 'BitcoinCash'
    symbol = 'BCH'
    network_name = 'mainnet'

    transaction_class = Transaction

    pubkey_address_prefix = int2byte(0x00)
    script_address_prefix = int2byte(0x05)
    extended_public_key_prefix = unhexlify('0488b21e')
    extended_private_key_prefix = unhexlify('0488ade4')

    default_fee_per_byte = 50


class UnverifiedHeaders(BaseHeaders):
    verify_bits_to_target = False


class RegTestLedger(MainNetLedger):
    headers_class = UnverifiedHeaders
    network_name = 'regtest'

    pubkey_address_prefix = int2byte(111)
    script_address_prefix = int2byte(196)
    extended_public_key_prefix = unhexlify('043587cf')
    extended_private_key_prefix = unhexlify('04358394')

    max_target = 0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    genesis_hash = '0f9188f13cb7b2c71f2a335e3a4fc328bf5beb436012afca590b1a11466e2206'
    genesis_bits = 0x207fffff
    target_timespan = 1
