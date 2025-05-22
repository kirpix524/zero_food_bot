# app/init_repositories.py

from repository.dish_repo import DishRepository, DishRepo
from storage.dish_storage import DishStorage


def init_repositories(bot, storage_list):
    # Инициализация хранилища блюд
    dish_storage = storage_list["dish_storage"]

    # Создание репозитория блюд
    bot.set_dish_repository(DishRepository(dish_storage))

    # Загрузка тестовых данных
    DishRepo.initialize(dish_storage)