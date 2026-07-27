import requests


class APIClient:
    def __init__(self, base_url, timeout=5):
        self.base_url = base_url
        self.timeout = timeout

    def get(self, path):
        return requests.get(f"{self.base_url}{path}", timeout=self.timeout)
