from qsnark_python_sdk.http.request import Request


class Account(Request):
    __API_CREATE_ACCOUNT = '/dev/account/create'

    def __init__(self):
        pass

    def create_account(self):
        return self.get(self.__API_CREATE_ACCOUNT)
