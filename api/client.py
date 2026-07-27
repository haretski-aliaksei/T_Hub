import requests

from constants.api.settings import API_REQUEST_TIMEOUT_SECONDS


class APIClient:
    def __init__(self, base_url, timeout=API_REQUEST_TIMEOUT_SECONDS):
        self.base_url = base_url
        self.timeout = timeout

    def get(self, path, params=None):
        return requests.get(
            f"{self.base_url}{path}",
            params=params,
            timeout=self.timeout,
        )
