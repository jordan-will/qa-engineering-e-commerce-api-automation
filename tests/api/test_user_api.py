from src.clients.user_client import UserClient


def test_create_user_with_test_data(user_client, users_data):
    user_data = users_data[0]

    response = user_client.create_user(user_data)

    assert response.status_code == 201