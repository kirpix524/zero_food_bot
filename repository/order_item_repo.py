from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from storage.order_items_storage import OrderItemStorage
    from models.order_item import OrderItem


class OrderItemRepository:
    def __init__(self, storage: 'OrderItemStorage') -> None:
        self._storage: 'OrderItemStorage' = storage

    def add_item(self, order_id: int, dish_id: int, quantity: int) -> None:
        pass

    def update_quantity(self, item_id: int, quantity: int) -> None:
        pass

    def get_by_order(self, order_id: int) -> List[OrderItem]:
        pass

    def delete_item(self, item_id: int) -> None:
        pass