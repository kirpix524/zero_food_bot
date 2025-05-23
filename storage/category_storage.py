from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.category import Category
    from storage.db_session import DBSession


class CategoryStorage:
    def __init__(self, db_session: 'DBSession', sql_data: dict[str, str]) -> None:
        self._db_session = db_session
        self._sql_data = sql_data  #данные по названиям табличек, пути к БД и т.п.
        self._init_table()

    def _init_table(self) -> None:
        pass

    def save(self, category: 'Category') -> None:
        pass

    def load_by_id(self, id: int) -> Optional['Category']:
        pass

    def load_all(self) -> List['Category']:
        return []

    def del_all(self) -> None:
        pass