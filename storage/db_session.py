import sqlite3
from sqlite3 import Connection

class DBSession:
    def __init__(self, db_path: str) -> None:
        """Инициализирует подключение к базе данных SQLite по указанному пути."""
        self._db_path: str = db_path
        self._connection: Connection = sqlite3.connect(self._db_path)

    def get_session(self) -> Connection:
        """Возвращает текущую сессию (соединение) с базой данных."""
        return self._connection

    def close_connection(self) -> None:
        """Закрывает соединение с базой данных."""
        if self._connection:
            self._connection.close()
