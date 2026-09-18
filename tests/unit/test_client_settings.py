from src.clients.auth_client import AuthClient
from src.clients.order_client import OrderClient
from src.clients.product_client import ProductClient
from src.clients.user_client import UserClient

def test_all_clients_use_settings():
    clients = [
        AuthClient(),
        UserClient(),
        ProductClient(),
        OrderClient()
    ]

    for client in clients:
        assert client.base_url == "https://dummyjson.com"
        assert client.timeout == 5