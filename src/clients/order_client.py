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
        payload = self.to_api_payload(order_data)

        return self.post(
            "/carts/add",
            json=payload,
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

    def to_api_payload(self, order_data):
        return {
            "userId": order_data["user_id"],
            "products": [
                {
                    "id": order_data["product_id"],
                    "quantity": order_data["quantity"],
                }
            ],
        }