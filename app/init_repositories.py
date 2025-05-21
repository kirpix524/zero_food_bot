from typing import Any

from app.bot import ZeroFoodBot
from repository.category_repo import CategoryRepository
from repository.dish_repo import DishRepo, DishRepository


def init_repositories(bot: ZeroFoodBot, storage_list: dict[str, Any]) -> None:
    dish_storage = storage_list["dish_storage"]
    category_storage = storage_list["category_storage"]

    dish_repo = DishRepository(dish_storage)
    category_repo = CategoryRepository(category_storage)

    bot.set_dish_storage(dish_storage)
    bot.set_dish_repository(dish_repo)
    bot.set_category_repository(category_repo)

    # Заполняем тестовые данные
    DishRepo.initialize(dish_storage)