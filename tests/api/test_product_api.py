from src.clients.product_client import ProductClient
from src.models.product import Product
from src.utils.data_loader import load_model

def test_get_product_returns_product():
    client = ProductClient()

    product = client.get_product(1)

    assert isinstance(product, Product)
    assert product.id == 1
    assert product.name 
    assert product.price > 0
    assert product.stock >= 0



