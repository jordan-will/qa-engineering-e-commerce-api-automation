from unittest.mock import Mock
from src.clients.product_client import ProductClient

def test_get_products():
    client = ProductClient()

    mock_response = Mock()
    client.get = Mock(return_value=mock_response)

    response = client.get_products()

    client.get.assert_called_once_with("/products")

    assert response == mock_response

def test_get_product():
    client = ProductClient()

    mock_response = Mock()
    client.get = Mock(return_value=mock_response)

    response = client.get_product(1)

    client.get.assert_called_once_with("/products/1")

    assert response == mock_response