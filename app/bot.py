from telebot import TeleBot

from repository.category_repo import CategoryRepository


class ZeroFoodBot(TeleBot):
    def __init__(self, token: str) -> None:
        super().__init__(token)
        self._category_repository: CategoryRepository = None  # type: ignore

    def set_category_repository(self, repository: CategoryRepository) -> None:
        """
        Сохраняет репозиторий категорий в контексте бота.
        """
        self._category_repository = repository

    def get_category_repository(self) -> CategoryRepository:
        """
        Возвращает ранее сохранённый репозиторий категорий.
        """
        if self._category_repository is None:
            raise ValueError("CategoryRepository не установлен")
        return self._category_repository