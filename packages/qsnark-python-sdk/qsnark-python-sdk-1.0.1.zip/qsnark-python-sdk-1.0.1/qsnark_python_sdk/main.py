from qsnark_python_sdk.api.access_token import AccessToken
from qsnark_python_sdk.api.account import Account
from qsnark_python_sdk.api.block import Block
from qsnark_python_sdk.api.contract import Contract
from qsnark_python_sdk.api.transaction import Transaction


class QsnarkSDK(AccessToken, Account, Block, Contract, Transaction):
    def __init__(self, options):
        if ('phone' not in options):
            raise ValueError('[phone] argument can not be empty')

        if ('password' not in options):
            raise ValueError('[password] argument can not be empty')

        if ('client_id' not in options):
            raise ValueError('[client_id] argument can not be empty')

        if ('client_secret' not in options):
            raise ValueError('[client_secret] argument can not be empty')

        self._token_auth_data = options
        self.get_access_token()

        self._client_id = options['client_id']
        self._client_secret = options['client_secret']
