import requests
from time import time


class AccessToken:
    def __init__(self, request, update_interval=30):
        self._request = request
        self._last_update = 0
        self._update_interval = update_interval
        self._token = self.get()

    def get(self):
        if time() - self._last_update < self._update_interval:
            return self._token

        s = requests.Session()
        response = s.send(self._request)
        token = response.json()['access_token']
        self._last_update = time()

        return token
