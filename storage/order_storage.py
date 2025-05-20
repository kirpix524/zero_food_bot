from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.order import Order
    from storage.db_session import DBSession


class OrderStorage:
    def __init__(self, db_session: 'DBSession', sql_data: dict[str, str]) -> None:
        self._db_session = db_session
        self._sql_data = sql_data
        self._init_table()

    def _init_table(self) -> None:
        pass

    def save(self, order: 'Order') -> None:
        pass

    def load_by_id(self, id: int) -> Optional['Order']:
        pass

    def load_by_user(self, user_id: int) -> List['Order']:
        pass