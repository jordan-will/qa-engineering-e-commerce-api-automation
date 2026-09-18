
from src.clients.auth_client import AuthClient
from src.clients.user_client import UserClient
from src.clients.product_client import ProductClient
from src.clients.order_client import OrderClient

# TEST SETTINGS
def test_settings_fixture(settings_fixture):
    assert settings_fixture.BASE_URL == "https://dummyjson.com"
    assert settings_fixture.REQUEST_TIMEOUT == 5

def test_base_client_fixture(base_client):
    assert base_client.base_url == "https://dummyjson.com"
    assert base_client.timeout == 5

# TEST API CLIENTS
def test_auth_client_fixture(auth_client):
    assert isinstance(auth_client, AuthClient)

def test_user_client_fixture(user_client):
    assert isinstance(user_client, UserClient)

def test_product_client_fixture(product_client):
    assert isinstance(product_client, ProductClient)

def test_order_client_fixture(order_client):
    assert isinstance(order_client, OrderClient)

def test_auth_token(auth_token):
    assert isinstance(auth_token, str)
    assert auth_token

# TEST DATA

def test_users_data(users_data):
    assert isinstance(users_data, list)
    assert users_data

def test_products_data(products_data):
    assert isinstance(products_data, list)
    assert products_data

def test_orders_data(orders_data):
    assert isinstance(orders_data, list)
    assert orders_data

def test_users_data_structure(users_data):
    for user in users_data:
        assert "id" in user
        assert "name" in user
        assert "email" in user
        assert "password" in user

def test_products_data_structure(products_data):
    for product in products_data:
        assert "id" in product
        assert "name" in product
        assert "price" in product
        assert "stock" in product

def test_order_data_structure(orders_data):
    for order in orders_data:
        assert "id" in order
        assert "user_id" in order
        assert "product_id" in order
        assert "quantity" in order
        assert "total" in order
        assert "status" in order

