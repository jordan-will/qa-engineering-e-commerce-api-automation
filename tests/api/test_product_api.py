from src.clients.product_client import ProductClient
from src.models.product import Product
from src.utils.data_loader import load_model, load_json

import pytest

def test_get_product_returns_product():
    client = ProductClient()

    product = client.get_product(1)

    assert isinstance(product, Product)
    assert product.id == 1
    assert product.name 
    assert product.price > 0
    assert product.stock >= 0

products = load_json("tests/data/products.json")

@pytest.mark.parametrize(
    "product_data",
    products
)
def test_get_product_by_test_data(product_data):
    client = ProductClient()

    product = client.get_product(product_data["id"])

    assert product.id == product_data["id"]





