from telebot import TeleBot
from typing_extensions import Optional

from builders.category_builder import CategoryMenuBuilder
from repository.category_repo import CategoryRepository


class ZeroFoodBot(TeleBot):
    def __init__(self, token: str) -> None:
        super().__init__(token)
        self._category_repository: Optional[CategoryRepository] = None  # type: ignore
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

    @property
    def category_menu_builder(self) -> CategoryMenuBuilder:
        return self._category_menu_builder