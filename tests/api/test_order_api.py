from src.clients.order_client import OrderClient
from src.utils.data_loader import load_json


def test_create_order_with_test_data():
    orders = load_json("tests/data/orders.json")

    order_data = orders[0]

    client = OrderClient()

    response = client.create_order(order_data)

    assert response.status_code == 201