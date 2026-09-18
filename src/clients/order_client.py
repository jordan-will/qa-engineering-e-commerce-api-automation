from src.clients.base_client import BaseClient
from src.models.order import Order

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
        response =  self.get(f"/carts/{order_id}")
        self.handle_response(response)

        return self.to_order(response.json())

    def to_order(self, data):
        prodcuct = data["products"][0]

        return Order(
            id=data["id"],
            user_id=data["userId"],
            product_id=prodcuct["id"],
            quantity=prodcuct["quantity"],
            total=data["total"],
            status="retrieved"
        )