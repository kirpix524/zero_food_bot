from telebot import TeleBot
from typing import Any, Dict,Optional

from builders.category_builder import CategoryMenuBuilder
from repository.category_repo import CategoryRepository
from repository.dish_repo import DishRepository


class ZeroFoodBot(TeleBot):
    def __init__(self, token):
        super().__init__(token)
        self._category_repository: Optional[CategoryRepository] = None  # type: ignore
        self._dish_repository: Optional[DishRepository] = None
        self._category_menu_builder: Optional[CategoryMenuBuilder] = None

    def set_category_repository(self, repository: CategoryRepository) -> None:
        """
        Сохраняет репозиторий категорий в контексте бота.
        """
        self._category_repository = repository
        self._category_menu_builder = CategoryMenuBuilder(repository)

    def get_category_repository(self) -> CategoryRepository | None:
        """
        Возвращает ранее сохранённый репозиторий категорий.
        """
        return self._category_repository
    
    def set_dish_repository(self, repo: DishRepository) -> None:
        self._dish_repository = repo

    def get_dish_repository(self) -> DishRepository | None:
        return self._dish_repository

    @property
    def category_menu_builder(self) -> CategoryMenuBuilder:
        return self._category_menu_builder