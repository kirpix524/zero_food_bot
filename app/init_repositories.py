from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from app.bot import ZeroFoodBot
from repository.dish_repo import DishRepository


def init_repositories(bot: 'ZeroFoodBot', storage_list: dict[str, Any]) -> None:
    # Инициализация хранилища блюд
    category_storage = storage_list["category_storage"]
    dish_storage = storage_list["dish_storage"]
    feedback_storage = storage_list["feedback_storage"]
    order_items_storage = storage_list["order_item_storage"]
    order_storage = storage_list["order_storage"]
    user_storage = storage_list["user_storage"]

    # Создание репозитория блюд
    bot.set_dish_repository(DishRepository(dish_storage))

    # Загрузка тестовых данных
    #DishRepo.initialize(dish_storage)