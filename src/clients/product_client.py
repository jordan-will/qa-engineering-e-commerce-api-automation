from src.clients.base_client import BaseClient

class ProductClient(BaseClient):

    def get_products(self):
        return self.get("/products")

    def get_product(self, product_id):
        return self.get(f"/products/{product_id}")

    

    