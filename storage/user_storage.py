from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models.user import User
    from storage.db_session import DBSession


class UserStorage:
    def __init__(self, db_session: 'DBSession', sql_data: dict[str, str]) -> None:
        self._db_session = db_session
        self._sql_data = sql_data
        self._init_table()

    def _init_table(self) -> None:
        pass

    def save(self, user: 'User') -> None:
        pass

    def load_by_telegram_id(self, telegram_id: int) -> Optional['User']:
        pass
