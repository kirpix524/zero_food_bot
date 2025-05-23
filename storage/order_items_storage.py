from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.order_item import OrderItem
    from storage.db_session import DBSession


class OrderItemStorage:
    def __init__(self, db_session: 'DBSession', sql_data: dict[str, str]) -> None:
        self._db_session = db_session
        self._sql_data = sql_data
        self._init_table()

    def _init_table(self) -> None:
        pass

    def save(self, item: 'OrderItem') -> None:
        pass

    def delete(self, item_id: int) -> None:
        pass

    def load_all(self) -> List['OrderItem']:
        return []

    def load_by_order(self, order_id: int) -> List['OrderItem']:
        pass