import os

from shortest_api_client.auth.auth_helper import AuthHelper
from shortest_api_client.sec.sec_helper import SECHelper

class ShortestLibrary:
    def __init__(self):
        self._config_id = os.getenv('CONFIGURATION_ID')
        self._host = os.getenv('HOST', 'https://shortesttrack.com')
        self._refresh_token = os.getenv('SEC_REFRESH_TOKEN')
        self._access_token = AuthHelper(self._host).get_access_token_from_refresh_token(self._refresh_token)

    def get_script_parameters(self):
        sec = SECHelper(self._config_id).get_sec(self._host, self._access_token.get())
        return sec['parameters']
    


