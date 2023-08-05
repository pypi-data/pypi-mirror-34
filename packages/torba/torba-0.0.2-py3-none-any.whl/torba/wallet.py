import stat
import json
import os
from typing import List

import torba.baseaccount
import torba.baseledger


class Wallet:
    """ The primary role of Wallet is to encapsulate a collection
        of accounts (seed/private keys) and the spending rules / settings
        for the coins attached to those accounts. Wallets are represented
        by physical files on the filesystem.
    """

    def __init__(self, name='Wallet', accounts=None, storage=None):
        # type: (str, List[torba.baseaccount.BaseAccount], WalletStorage) -> None
        self.name = name
        self.accounts = accounts or []  # type: List[torba.baseaccount.BaseAccount]
        self.storage = storage or WalletStorage()

    def generate_account(self, ledger):
        # type: (torba.baseledger.BaseLedger) -> torba.baseaccount.BaseAccount
        account = ledger.account_class.generate(ledger, u'torba')
        self.accounts.append(account)
        return account

    @classmethod
    def from_storage(cls, storage, manager):  # type: (WalletStorage, 'WalletManager') -> Wallet
        json_dict = storage.read()

        accounts = []
        for account_dict in json_dict.get('accounts', []):
            ledger = manager.get_or_create_ledger(account_dict['ledger'])
            account = ledger.account_class.from_dict(ledger, account_dict)
            accounts.append(account)

        return cls(
            name=json_dict.get('name', 'Wallet'),
            accounts=accounts,
            storage=storage
        )

    def to_dict(self):
        return {
            'version': WalletStorage.LATEST_VERSION,
            'name': self.name,
            'accounts': [a.to_dict() for a in self.accounts]
        }

    def save(self):
        self.storage.write(self.to_dict())

    @property
    def default_account(self):
        for account in self.accounts:
            return account


class WalletStorage:

    LATEST_VERSION = 1

    def __init__(self, path=None, default=None):
        self.path = path
        self._default = default or {
            'version': self.LATEST_VERSION,
            'name': 'My Wallet',
            'accounts': []
        }

    def read(self):
        if self.path and os.path.exists(self.path):
            with open(self.path, 'r') as f:
                json_data = f.read()
                json_dict = json.loads(json_data)
                if json_dict.get('version') == self.LATEST_VERSION and \
                        set(json_dict) == set(self._default):
                    return json_dict
                else:
                    return self.upgrade(json_dict)
        else:
            return self._default.copy()

    def upgrade(self, json_dict):
        json_dict = json_dict.copy()
        version = json_dict.pop('version', -1)
        if version == -1:
            pass
        upgraded = self._default.copy()
        upgraded.update(json_dict)
        return json_dict

    def write(self, json_dict):

        json_data = json.dumps(json_dict, indent=4, sort_keys=True)
        if self.path is None:
            return json_data

        temp_path = "%s.tmp.%s" % (self.path, os.getpid())
        with open(temp_path, "w") as f:
            f.write(json_data)
            f.flush()
            os.fsync(f.fileno())

        if os.path.exists(self.path):
            mode = os.stat(self.path).st_mode
        else:
            mode = stat.S_IREAD | stat.S_IWRITE
        try:
            os.rename(temp_path, self.path)
        except:
            os.remove(self.path)
            os.rename(temp_path, self.path)
        os.chmod(self.path, mode)
