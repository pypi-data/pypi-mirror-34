from urlobject import URLObject
import requests
import json


class SECHelper:
    def __init__(self, config_id):
        self._config_id = config_id

    def get_sec(self, host, access_token):
        url = URLObject(host).add_path('api/metadata/script-execution-configurations/{}'.
                                       format(self._config_id))
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        response = requests.get(url, headers=headers)

        return json.loads(response.content)

    def get_content(self, host, access_token):
        url = URLObject(host).add_path('api/data/script-execution-configurations/{}/script/content'.
                                       format(self._config_id))
        headers = { 'Authorization': 'Bearer {}'.format(access_token)}
        response = requests.get(url, headers=headers)

        return response.content
