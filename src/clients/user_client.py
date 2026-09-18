from src.clients.base_client import BaseClient
from src.models.user import User

class UserClient(BaseClient):

    def get_user(self, user_id):
        response = self.get(f"/users/{user_id}")
        self.handle_response(response)

        return self.to_user(response.json())

    def create_user(self, user_data):
        return self.post(
            "/users/add",
            json=user_data
        )

    def update_user(self, user_id, user_data):
        return self.put(
            f"/users/{user_id}",
            json=user_data
        )

    def delete_user(self, user_id):
        return self.delete(f"/users/{user_id}")

    def to_user(self, data):
        return User(
            id=data["id"],
            name=f"{data["firstName"]} {data["lastName"]}",
            email=data["email"],
            password=data["password"]
        )

    