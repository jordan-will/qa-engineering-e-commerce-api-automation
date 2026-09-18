import requests
from config import settings


class BaseClient:

    def __init__(self, token = None):
        self.base_url = settings.BASE_URL.rstrip("/")
        self.timeout = settings.REQUEST_TIMEOUT
        self.session = requests.Session()
        self.token = token

    def get_headers(self, headers = None):
        default_headers = {}

        if self.token:
            default_headers["Authorization"] = f"Bearer {self.token}"

        if headers:
            default_headers.update(headers)

        return default_headers

    def get(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"

        headers = self.get_headers(kwargs.pop("headers", None))

        return self.session.get(
            url,
            timeout=self.timeout,
            headers=headers,
            **kwargs
        )

    def post(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"

        headers = self.get_headers(kwargs.pop("headers", None))

        return self.session.post(
            url,
            timeout=self.timeout,
            headers=headers,
            **kwargs
        )

    def put(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"

        headers = self.get_headers(kwargs.pop("headers", None))

        return self.session.put(
            url,
            timeout=self.timeout,
            headers=headers,
            **kwargs
        )

    def delete(self, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"

        headers = self.get_headers(kwargs.pop("headers", None))

        return self.session.delete(
            url,
            timeout=self.timeout,
            headers=headers,
            **kwargs
        )

    def handle_response(self, response):
        response.raise_for_status()
        return response