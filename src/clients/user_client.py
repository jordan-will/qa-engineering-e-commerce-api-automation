from src.clients.base_client import BaseClient

class UserClient(BaseClient):

    def get_user(self, user_id):
        return self.get(f"/users/{user_id}")

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

    