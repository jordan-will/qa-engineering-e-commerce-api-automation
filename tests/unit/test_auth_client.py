from unittest.mock import Mock
from src.clients.auth_client import AuthClient

def test_login():
    client = AuthClient()

    mock_response = Mock()
    mock_response.json.return_value = {
        "accessToken" : "test-token"
    }

    client.post = Mock(return_value=mock_response)

    response = client.login("emilys", "emilyspass")

    client.post.assert_called_once_with(
        "/auth/login",
        json={
            "username": "emilys",
            "password": "emilyspass"
        }
    )

    assert response == mock_response
    assert client.token == "test-token"

def test_token_is_none_before_login():
    client = AuthClient()

    assert client.token is None