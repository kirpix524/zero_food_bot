from datetime import datetime
from typing import Optional

from models.enums import OrderStatus, PaymentMethod
from models.order_item import OrderItem


class Order:
    def __init__(self, id: int, user_id: int, status: OrderStatus, created_at: datetime, payment_method: Optional[PaymentMethod]):
        self._id: int = id
        self._user_id: int = user_id
        self._status: OrderStatus = status
        self._payment_method: Optional[PaymentMethod] = payment_method
        self._created_at: datetime = created_at
        self._items: list[OrderItem] = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def status(self) -> OrderStatus:
        return self._status

    @status.setter
    def status(self, status: OrderStatus):
        self._status = status

    @property
    def payment_method(self) -> PaymentMethod | None:
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method: PaymentMethod):
        self._payment_method = payment_method

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def items(self) -> list[OrderItem]:
        return self._items

    @items.setter
    def items(self, items: list[OrderItem]):
        self._items = items

    def update_item(self, item: OrderItem):
        self.del_item(item)
        self._items.append(item)

    def get_item_by_dish_id(self, dish_id: int) -> Optional[OrderItem]:
        for item in self._items:
            if item.dish_id == dish_id:
                return item
        return None

    def del_item(self, item: OrderItem) -> None:
        for i in self._items:
            if i.id == item.id:
                self._items.remove(i)