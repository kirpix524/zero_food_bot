from telebot import TeleBot
from typing import Any, Dict

class ZeroFoodBot(TeleBot):
    def __init__(self, token):
        super().__init__(token)
        self._repositories: Dict[str, Any] = {}

    def set_category_repository(self, repo):
        self._repositories["category"] = repo

    def set_dish_repository(self, repo):
        self._repositories["dish"] = repo

    def get_dish_repository(self):
        return self._repositories.get("dish")

    def set_dish_storage(self, storage):
        self._repositories["dish_storage"] = storage

    def get_dish_storage(self):
        return self._repositories.get("dish_storage")