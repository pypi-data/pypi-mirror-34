from urlobject import URLObject
import requests
from requests.auth import HTTPBasicAuth

from shortest_api_client.auth.access_token import AccessToken


class AuthHelper:
    def __init__(self, host):
        self._host = host

    def get_access_token_from_username(self, username, password, company_id):
        f_root = [
            ('grant_type', 'password'), ('username', username),
            ('password', password), ('company_id', company_id)
        ]
        url = URLObject(self._host).add_path('/api/uaa/authenticate')

        req = requests.Request('POST', url, data=f_root).prepare()

        return AccessToken(req)

    def get_access_token_from_refresh_token(self, refresh_token):
        data = 'grant_type=refresh_token&client_id=script&refresh_token={}'.format(refresh_token)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        req = requests.Request('POST', URLObject(self._host).add_path('/oauth/token'),
                               data=data, headers=headers,
                               auth=HTTPBasicAuth('script', 'noMatter', )).prepare()

        return AccessToken(req)
