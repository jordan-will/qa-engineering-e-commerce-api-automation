from src.clients.user_client import UserClient
from src.utils.data_loader import load_json


def test_create_user_with_test_data():
    users = load_json("tests/data/users.json")

    user_data = users[0]

    client = UserClient()

    response = client.create_user(user_data)

    assert response.status_code == 201