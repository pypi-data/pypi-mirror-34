"""
封装请求方法
"""
import requests
import json


class Request(object):
    __BASE_URL = 'https://dev.hyperchain.cn/v1'
    __API_REFRESH_ACCESS_TOKEN = '/token/rtoken'

    _access_token = ''
    _refresh_token = ''
    _client_id = ''
    _client_secret = ''

    def __init__(self):
        pass

    def handle_result(self, options):
        response = requests.request(
            options['method'],
            options['url'],
            headers=options['headers'],
            data=options['data']
        )

        result = json.loads(response.content)

        if ('Code' in result and abs(result['Code']) == 1008):
            # update auth token
            self._refresh_access_token()

            # request again
            self.handle_result(options)

        return result

    def get(self, url):
        options = {
            'method': 'get',
            'url': self.__BASE_URL + url,
            'headers': {
                'Authorization': self._access_token,
            },
            'data': None
        }

        return self.handle_result(options)

    def post_form(self, url, data={}):
        options = {
            'method': 'post',
            'url': self.__BASE_URL + url,
            'headers': {
                'Authorization': self._access_token,
                'Content-type': 'application/x-www-form-urlencoded'
            },
            'data': data
        }

        return self.handle_result(options)

    def post_json(self, url, data={}):
        options = {
            'method': 'post',
            'url': self.__BASE_URL + url,
            'headers': {
                'Authorization': self._access_token,
                'Content-type': 'application/json'
            },
            'data': json.dumps(data)
        }

        return self.handle_result(options)

    def _refresh_access_token(self):
        auth_data = {
            'refresh_token': self._refresh_token,
            'client_id': self._client_id,
            'client_secret': self._client_secret
        }
        result = self.post_form(self.__API_REFRESH_ACCESS_TOKEN, auth_data)

        if ('access_token' not in result):
            raise KeyError(str(result))
        else:
            self._access_token = result['access_token']

        if ('refresh_token' not in result):
            raise KeyError(str(result))
        else:
            self._refresh_token = result['refresh_token']

        return result
