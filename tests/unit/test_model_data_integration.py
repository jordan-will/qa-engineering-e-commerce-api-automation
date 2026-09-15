from src.models.order import Order
from src.models.product import Product
from src.models.user import User
from src.utils.data_loader import load_model

USER_FILE = "tests/data/users.json"
PRODUCTS_FILE = "tests/data/products.json"
ORDER_FILE = "tests/data/orders.json"

def test_load_users():
    users = load_model(USER_FILE, User)

    assert len(users) == 2
    assert all(isinstance(user, User) for user in users)

def test_load_products():
    products = load_model(PRODUCTS_FILE, Product)

    assert len(products) == 2
    assert all(isinstance(product, Product) for product in products)

def test_load_orders():
    orders = load_model(ORDER_FILE, Order)

    assert len(orders) == 2
    assert all(isinstance(order, Order) for order in orders)
    