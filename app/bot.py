from telebot import TeleBot
from typing import Any, Dict,Optional

from builders.category_builder import CategoryMenuBuilder
class ZeroFoodBot(TeleBot):
    def __init__(self, token):
        super().__init__(token)
        self._category_repository: Optional[CategoryRepository] = None  # type: ignore
        self._category_menu_builder: Optional[CategoryMenuBuilder] = None

    def set_category_repository(self, repo):
        self._repositories["category"] = repo
        self._category_menu_builder = CategoryMenuBuilder(repository)

def get_category_repository(self) -> CategoryRepository | None:
        """
        Возвращает ранее сохранённый репозиторий категорий.
        """
        return self._category_repository
    
    def set_dish_repository(self, repo):
        self._repositories["dish"] = repo

    def get_dish_repository(self):
        return self._repositories.get("dish")

    def set_dish_storage(self, storage):
        self._repositories["dish_storage"] = storage

    def get_dish_storage(self):
        return self._repositories.get("dish_storage")

    @property
    def category_menu_builder(self) -> CategoryMenuBuilder:
        return self._category_menu_builder