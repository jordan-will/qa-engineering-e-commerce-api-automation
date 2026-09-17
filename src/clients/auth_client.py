from src.clients.base_client import BaseClient

class AuthClient(BaseClient):

    def __init__(self):
        super().__init__()
        self.token = None

    def login(self, username, password):
        payload = {
            "username": username,
            "password": password
        }

        response =  self.post(
            "/auth/login",
            json=payload
        )

        self.token = response.json()["accessToken"]

        return response

