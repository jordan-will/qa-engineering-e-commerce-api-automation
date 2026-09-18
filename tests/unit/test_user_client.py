from unittest.mock import Mock
from src.clients.user_client import UserClient
from src.models.user import User

def test_get_user():
    client = UserClient()

    mock_response = Mock()
    mock_response.json.return_value = {
        "id" :  1,
        "firstName" : "John",
        "lastName" : "Doe",
        "email" : "john@example.com",
        "password" : "secret123"
    }

    client.get = Mock(return_value=mock_response)
    client.handle_response = Mock(return_value=mock_response)

    user = client.get_user(1)

    client.get.assert_called_once_with("/users/1")
    client.handle_response.assert_called_once_with(mock_response)

    assert isinstance(user, User)
    assert user.id == 1
    assert user.name == "John Doe"
    assert user.email == "john@example.com"
    assert user.password == "secret123"

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

def test_to_user():
    client = UserClient()

    data = {
        "id":1,
        "firstName" : "John",
        "lastName" : "Doe",
        "email" : "john@example.com",
        "password" : "secret123"
    }

    user = client.to_user(data)

    assert isinstance(user, User)
    assert user.id == 1
    assert user.name == "John Doe"
    assert user.email == "john@example.com"
    assert user.password == "secret123"