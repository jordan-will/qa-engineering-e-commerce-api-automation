from dataclasses import dataclass

@dataclass
class Order:
    id: int
    user_id: int
    product_id: int
    quantity: int
    total: float
    status: str