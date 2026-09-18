from src.clients.order_client import OrderClient

def test_create_order_with_test_data(order_client, orders_data):
    order_data = orders_data[0]

    response = order_client.create_order(order_data)

    assert response.status_code == 201