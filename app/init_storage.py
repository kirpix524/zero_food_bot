from typing import Any

from app.bot import ZeroFoodBot
from config import SQL_DATA
from storage.category_storage import CategoryStorage
from storage.db_session import DBSession
from storage.feedback_storage import FeedbackStorage


def init_storage(db_session: DBSession) -> dict[str, Any]:
    category_storage = CategoryStorage(db_session,SQL_DATA)
    feedback_storage = FeedbackStorage(db_session,SQL_DATA)
    return {"category_storage": category_storage,
            "feedback_storage": feedback_storage}