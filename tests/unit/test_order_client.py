from unittest.mock import Mock
from src.models.order import Order

from src.clients.order_client import OrderClient

def test_create_order():
    client = OrderClient()

    mock_response = Mock()
    client.post = Mock(return_value=mock_response)

    order_data = {
        "userId": 1,
        "products": [
            {
                "id": 1,
                "quantity": 2,
            }
        ],
    }

    response = client.create_order(order_data)

    client.post.assert_called_once_with(
        "/carts/add",
        json=order_data
    )

    assert response == mock_response

def test_get_order():
    client = OrderClient()

    mock_response = Mock()
    mock_response.json.return_value = {
        "id" : 1,
        "userId" : 1,
        "products" : [
            {
                "id" : 1,
                "quantity" : 2
            }
        ],
        "total" : 5000.00
    }

    
    client.get = Mock(return_value=mock_response)
    client.handle_response = Mock(return_value=mock_response)

    order = client.get_order(1)

    client.get.assert_called_once_with("/carts/1")
    client.handle_response.assert_called_once_with(mock_response)

    assert isinstance(order, Order)
    assert order.id == 1
    assert order.user_id == 1 
    assert order.product_id == 1
    assert order.quantity == 2
    assert order.total == 5000.00
    assert order.status == "retrieved"

def test_to_order():
    client = OrderClient()

    data = {
        "id" : 1,
        "userId" : 1,
        "products" : [
                {
                    "id" : 1,
                    "quantity" : 2
                }
            ],
        "total" : 5000.00
    }

    order = client.to_order(data)

    assert isinstance(order, Order)
    assert order.id == 1
    assert order.user_id == 1
    assert order.product_id == 1
    assert order.quantity == 2
    assert order.total == 5000.00
    assert order.status == "retrieved"