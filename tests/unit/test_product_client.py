from unittest.mock import Mock
from src.clients.product_client import ProductClient
from src.models.product import Product

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
    mock_response.json.return_value = {
        "id":1,
        "title":"Laptop",
        "price":2500.00,
        "stock":10
    }

    client.get = Mock(return_value=mock_response)
    client.handle_response = Mock(return_value=mock_response)

    product = client.get_product(1)

    client.get.assert_called_once_with("/products/1")
    client.handle_response.assert_called_once_with(mock_response)

    assert isinstance(product, Product)
    assert product.id == 1
    assert product.name == "Laptop"
    assert product.price == 2500.00
    assert product.stock == 10

def test_to_product():
    client = ProductClient()

    data = {
        "id": 1,
        "title":"Laptop",
        "price":2500.00,
        "stock":10
    }

    product = client.to_product(data)

    assert isinstance(product, Product)
    assert product.id == 1
    assert product.name == "Laptop"
    assert product.price == 2500.00
    assert product.stock == 10