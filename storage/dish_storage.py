from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from storage.db_session import DBSession
    from models.dish import Dish

class DishStorage:
    def __init__(self, db_session: 'DBSession', sql_data: dict[str, str]) -> None:
        self._db_session = db_session
        self._sql_data = sql_data
        self._init_table()

    def _init_table(self) -> None:
        pass

    def save(self, dish: 'Dish') -> None:
        pass

    def load_by_id(self, id: int) -> Optional['Dish']:
        pass

    def load_by_category(self, category_id: int) -> List['Dish']:
        pass