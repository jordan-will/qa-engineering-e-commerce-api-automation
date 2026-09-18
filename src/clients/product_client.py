from src.clients.base_client import BaseClient
from src.models.product import Product

class ProductClient(BaseClient):

    def get_products(self):
        return self.get("/products")

    def get_product(self, product_id):
        response =  self.get(f"/products/{product_id}")
        self.handle_response(response)

        return self.to_product(response.json())

    def to_product(self, data):
        return Product(
            id=data["id"],
            name=data["title"],
            price=data["price"],
            stock=data["stock"]
        )

    

    