import pytest

from config import settings

from src.clients.base_client import BaseClient
from src.clients.auth_client import AuthClient
from src.clients.user_client import UserClient
from src.clients.product_client import ProductClient
from src.clients.order_client import OrderClient

from pathlib import Path

from src.utils.data_loader import load_json

TEST_DATA_DIR = Path(__file__).parent / "data"

# CONFIG FIXTURES
@pytest.fixture(scope="session")
def settings_fixture():
    return settings

@pytest.fixture(scope="session")
def base_client():
    return BaseClient()


# API CLIENT FIXTURES
@pytest.fixture(scope="session")
def auth_client():
    return AuthClient()

@pytest.fixture(scope="session")
def user_client():
    return UserClient()

@pytest.fixture(scope="session")
def product_client():
    return ProductClient()

@pytest.fixture(scope="session")
def order_client():
    return OrderClient()

@pytest.fixture(scope="session")
def auth_token(auth_client, settings_fixture):
    response = auth_client.login(
        settings_fixture.API_USERNAME,
        settings_fixture.API_PASSWORD
    )

    return response.json()["accessToken"]

# DATA FIXTURES
@pytest.fixture(scope="session")
def users_data():
    return load_json(
        TEST_DATA_DIR / "users.json"
    )

@pytest.fixture(scope="session")
def products_data():
    return load_json(
        TEST_DATA_DIR / "products.json"
    )

@pytest.fixture(scope="session")
def orders_data():
    return load_json(
        TEST_DATA_DIR / "orders.json"
    )