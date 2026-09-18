from unittest.mock import Mock
from src.models.order import Order

from src.clients.order_client import OrderClient

def test_create_order():
    client = OrderClient()

    mock_response = Mock()
    client.post = Mock(return_value=mock_response)

    order_data = {
        "id": 100,
        "user_id": 1,
        "product_id": 1,
        "quantity": 2,
        "total": 5000.00,
        "status": "pending",
    }

    response = client.create_order(order_data)

    expected_payload = {
        "userId": 1,
        "products": [
            {
                "id": 1,
                "quantity": 2,
            }
        ],
    }

    client.post.assert_called_once_with(
        "/carts/add",
        json=expected_payload,
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

def test_to_api_payload():
    client = OrderClient()

    order_data = {
        "id": 100,
        "user_id": 1,
        "product_id": 1,
        "quantity": 2,
        "total": 5000.00,
        "status": "pending",
    }

    payload = client.to_api_payload(order_data)

    assert payload == {
        "userId": 1,
        "products": [
            {
                "id": 1,
                "quantity": 2,
            }
        ],
    }