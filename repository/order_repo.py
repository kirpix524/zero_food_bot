from datetime import datetime
from typing import Optional, List, TYPE_CHECKING


from storage.order_storage import OrderStorage
from models.enums import OrderStatus
from models.order import Order


class OrderRepository:
    def __init__(self, storage: 'OrderStorage') -> None:
        self._storage = storage
        self._orders: List['Order'] = storage.load_all()

    def __get_new_id(self):
        if len(self._orders) == 0:
            return 1
        return max([order.id for order in self._orders])+1

    def get_in_cart(self, user_id: int) -> Optional['Order']:
        pass

    def create(self, user_id: int) -> 'Order':
        order = Order(id=self.__get_new_id(), user_id=user_id, status=OrderStatus.IN_CART, created_at=datetime.now(), payment_method=None)
        return order

    def save(self, order: 'Order') -> None:
        pass

    def update_status(self, order_id: int, status: 'OrderStatus') -> None:
        pass

    def get_all_by_user(self, user_id: int) -> List['Order']:
        pass