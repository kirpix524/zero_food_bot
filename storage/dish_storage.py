# storage/dish_storage.py

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

    def load_all(self) -> list['Dish']:
        pass

    def save_all(self, dishes: List['Dish']) -> None:
        pass

    def del_all(self) -> None:
        pass