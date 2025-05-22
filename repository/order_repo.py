from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from storage.order_storage import OrderStorage
    from models.enums import OrderStatus
    from models.order import Order


class OrderRepository:
    def __init__(self, storage: 'OrderStorage') -> None:
        self._storage = storage
        
    def get_in_cart(self, user_id: int) -> Optional['Order']:
        pass

    def create(self, user_id: int) -> Order:
        pass

    def update_status(self, order_id: int, status: 'OrderStatus') -> None:
        pass

    def get_all_by_user(self, user_id: int) -> List['Order']:
        pass


class OrderRepo:
    pass