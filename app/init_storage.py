from typing import Any

from app.bot import ZeroFoodBot
from config import SQL_DATA
from storage.category_storage import CategoryStorage
from storage.dish_storage import DishStorage
from storage.db_session import DBSession


def init_storage(db_session: DBSession) -> dict[str, Any]:
    category_storage = CategoryStorage(db_session, SQL_DATA)
    dish_storage = DishStorage(db_session, SQL_DATA)

    return {
        "category_storage": category_storage,
        "dish_storage": dish_storage
    }