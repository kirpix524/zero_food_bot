from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.feedback import Feedback
    from storage.db_session import DBSession


class FeedbackStorage:
    def __init__(self, db_session: 'DBSession', sql_data: dict[str, str]) -> None:
        self._db_session = db_session
        self._sql_data = sql_data
        self._init_table()

    def _init_table(self) -> None:
        pass

    def save(self, feedback: 'Feedback') -> None:
        pass

    def load_latest(self, n: int) -> List['Feedback']:
        pass

    def load_all(self) -> List['Feedback']:
        return []
