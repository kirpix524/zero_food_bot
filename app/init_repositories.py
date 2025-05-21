from typing import Any

from app.bot import ZeroFoodBot
from repository.category_repo import CategoryRepository


def init_repositories(bot: ZeroFoodBot, storage_list: dict[str, Any]) -> None:
    category_repository = CategoryRepository(storage_list["category_storage"])
    bot.set_category_repository(category_repository)