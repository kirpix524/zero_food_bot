from models.dish import Dish


class OrderItem:
    def __init__(self, id: int, order_id: int, dish_id: int, quantity: int):
        self._id = id
        self._order_id = order_id
        self._dish_id = dish_id
        self._quantity = quantity

    @property
    def id(self) -> int:
        return self._id

    @property
    def order_id(self) -> int:
        return self._order_id

    @property
    def dish_id(self) -> int:
        return self._dish_id

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self._quantity = quantity