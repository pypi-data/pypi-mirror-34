from qsnark_python_sdk.http.request import Request


class AccessToken(Request):
    _token_auth_data = {}
    __API_GET_ACCESS_TOKEN = '/token/gtoken'
    __API_REFRESH_ACCESS_TOKEN = '/token/rtoken'

    def __init__(self):
        pass

    def get_access_token(self):
        result = self.post_form(
            self.__API_GET_ACCESS_TOKEN,
            self._token_auth_data
        )

        if ('access_token' not in result):
            raise KeyError(str(result))
        else:
            self._access_token = result['access_token']

        if ('refresh_token' not in result):
            raise KeyError(str(result))
        else:
            self._refresh_token = result['refresh_token']

        return result

    def refresh_access_token(self):
        return self._refresh_access_token()
