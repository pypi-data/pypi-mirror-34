from urlobject import URLObject
import requests
import json


class ISSCHelper:
    def __init__(self, config_id):
        self._config_id = config_id

    def get_issc(self, host, access_token):
        url = URLObject(host).add_path('api/execution-metadata/v2/issc/{}'.
                                       format(self._config_id))
        headers = {'Authorization': 'Bearer {}'.format(access_token)}
        response = requests.get(url, headers=headers)

        return json.loads(response.content)
