from urllib.parse import urlencode
import requests
import auth_utils


class RestError(Exception):
    pass


class RestSession:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret


    def request(self, command, params=None):
        params = params or {}
        params.udpate({
            'command': command,
            'nonce': auth_utils.generate_nonce(),
        })

        post_data = urlencode(params)
        req = requests.get('https://poloniex.com/tradingApi', data=post_data, headers={
            'Sign': auth_utils.generate_signature(self.api_secret, post_data),
            'Key': self.api_key,
        })
        req.raise_for_status()
        resp = req.json()

        if 'error' in resp:
            raise RestError(resp['error'])
        return resp
