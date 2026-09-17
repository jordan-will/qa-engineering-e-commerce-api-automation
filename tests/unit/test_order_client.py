from unittest.mock import Mock

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
    client.get = Mock(return_value=mock_response)

    response = client.get_order(1)

    client.get.assert_called_once_with("/carts/1")

    assert response == mock_response