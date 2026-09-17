from unittest.mock import Mock
from src.clients.base_client import BaseClient

def test_get():
    client = BaseClient()

    client.session.get = Mock()

    client.get("/products")

    client.session.get.assert_called_once_with(
        "https://dummyjson.com/products",
        timeout=5
    )

def test_post():
    client = BaseClient()

    client.session.post = Mock()

    payload = {"title": "QA Product"}

    client.post("/products/add", json=payload)

    client.session.post.assert_called_once_with(
        "https://dummyjson.com/products/add",
        timeout=5,
        json=payload
    )


def test_put():
    client = BaseClient()

    client.session.put = Mock()

    payload = {"title": "Updated product"}

    client.put("/products/1", json=payload)

    client.session.put.assert_called_once_with(
        "https://dummyjson.com/products/1",
        timeout=5,
        json=payload
    )

def test_delete():
    client = BaseClient()

    client.session.delete = Mock()

    client.delete("/products/1")

    client.session.delete.assert_called_once_with(
        "https://dummyjson.com/products/1",
        timeout=5
    )
