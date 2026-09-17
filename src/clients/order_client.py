from src.clients.base_client import BaseClient

class OrderClient(BaseClient):
    order_data = {
        "userId": 1,
        "products": [
            {
                "id": 1,
                "quantity": 2
            }
        ]
    }

    def create_order(self, order_data):
        return self.post(
            "/carts/add",
            json=order_data
        )

    def get_order(self, order_id):
        return self.get(f"/carts/{order_id}")