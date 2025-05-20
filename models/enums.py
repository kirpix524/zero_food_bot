from enum import Enum

class OrderStatus(Enum):
    IN_CART = "IN_CART"
    PENDING = "PENDING"
    PREPARING = "PREPARING"
    DONE = "DONE"

class PaymentMethod(Enum):
    ONLINE = "ONLINE"
    CASH = "CASH"