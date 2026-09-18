from src.clients.product_client import ProductClient
from src.models.product import Product

def test_get_product_returns_product(product_client):
    #client = ProductClient()

    product = product_client.get_product(1)

    assert isinstance(product, Product)
    assert product.id == 1
    assert product.name 
    assert product.price > 0
    assert product.stock >= 0


def test_get_product_by_test_data(product_client, products_data):
    for product_data in products_data:
        product = product_client.get_product(product_data["id"])

        assert product.id == product_data["id"]





