from unittest.mock import Mock
from src.clients.user_client import UserClient

def test_get_user():
    client = UserClient()

    mock_response = Mock()
    client.get = Mock(return_value=mock_response)

    response = client.get_user(1)

    client.get.assert_called_once_with("/users/1")
    assert response == mock_response

def test_create_user():
    client = UserClient()

    mock_response = Mock()
    client.post = Mock(return_value=mock_response)

    user_data = {
        "firstname" : "QA",
        "lastname" : "Tester",
        "age" : 25 
    }

    response = client.create_user(user_data)

    client.post.assert_called_once_with(
        "/users/add",
        json=user_data
    )

    assert response == mock_response

def test_update_user():
    client = UserClient()

    mock_response = Mock()
    client.put = Mock(return_value=mock_response)

    user_data = {
        "firstname" : "Update"
    }

    response = client.update_user(1, user_data)

    client.put.assert_called_once_with(
        "/users/1",
        json=user_data
    )

    assert response == mock_response

def test_delete_user():
    client = UserClient()

    mock_response = Mock()
    client.delete = Mock(return_value=mock_response)

    response = client.delete_user(1)

    client.delete.assert_called_once_with("/users/1")

    assert response == mock_response