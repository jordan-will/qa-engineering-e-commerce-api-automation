from unittest.mock import Mock
from src.clients.base_client import BaseClient
import pytest

def test_get():
    client = BaseClient()

    client.session.get = Mock()

    client.get("/products")

    client.session.get.assert_called_once_with(
        "https://dummyjson.com/products",
        timeout=5,
        headers={}
    )

def test_post():
    client = BaseClient()

    client.session.post = Mock()

    payload = {"title": "QA Product"}

    client.post("/products/add", json=payload)

    client.session.post.assert_called_once_with(
        "https://dummyjson.com/products/add",
        timeout=5,
        json=payload,
        headers={}
    )

def test_put():
    client = BaseClient()

    client.session.put = Mock()

    payload = {"title": "Updated product"}

    client.put("/products/1", json=payload)

    client.session.put.assert_called_once_with(
        "https://dummyjson.com/products/1",
        timeout=5,
        json=payload,
        headers={}
    )

def test_delete():
    client = BaseClient()

    client.session.delete = Mock()

    client.delete("/products/1")

    client.session.delete.assert_called_once_with(
        "https://dummyjson.com/products/1",
        timeout=5,
        headers={}
    )

def test_get_headers_without_token():
    client = BaseClient()

    headers = client.get_headers()

    assert headers == {}

def test_get_headers_with_token():
    client = BaseClient(token="test-token")

    headers = client.get_headers()

    assert headers == {
        "Authorization" : "Bearer test-token"
    }

def test_get_headers_with_and_custom_token():
    client = BaseClient(token="test-token")

    headers = client.get_headers({
        "Content-Type" : "application/json"
    })

    assert headers == {
        "Authorization" : "Bearer test-token",
        "Content-Type" : "application/json"
    }

def test_handle_response():
    client = BaseClient()

    response = Mock()

    result = client.handle_response(response)

    response.raise_for_status.assert_called_once_with()

    assert result == response

def test_handle_response_raises_error():
    client = BaseClient()

    response = Mock()
    response.raise_for_status.side_effect = Exception("HTTP error")

    with pytest.raises(Exception, match="HTTP error"):
        client.handle_response(response)