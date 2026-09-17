import requests
from config import settings

class BaseClient:

    def __init__(self):
        self.base_url = settings.BASE_URL.rstrip("/")
        self.timeout = settings.REQUEST_TIMEOUT
        self.session= requests.Session()

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(
            url, 
            timeout=self.timeout
        )

    def post(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(
            url,
            timeout=self.timeout,
            **kwargs
        )

    def put(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"

        return self.session.put(
            url,
            timeout=self.timeout,
            **kwargs
        )

    def delete(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"

        return self.session.delete(
            url,
            timeout=self.timeout,
            **kwargs
        ) 