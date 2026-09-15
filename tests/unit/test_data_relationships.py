from src.models.order import Order
from src.models.product import Product
from src.models.user import User
from src.utils.data_loader import load_model

USERS_FILE = "tests/data/users.json"
PRODUCTS_FILE = "tests/data/products.json"
ORDERS_FILE = "tests/data/orders.json"

def test_order_reference_existing_user():
    users = load_model(USERS_FILE, User)
    orders = load_model(ORDERS_FILE, Order)

    user_ids = {user.id for user in users}
    assert all(order.user_id in user_ids for order in orders)

def test_orders_reference_existing_products():
    products = load_model(PRODUCTS_FILE, Product)
    orders = load_model(ORDERS_FILE, Order)

    product_ids = {product.id for product in products}
    assert all(order.product_id in product_ids for order in orders)