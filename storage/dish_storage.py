# storage/dish_storage.py

from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from storage.db_session import DBSession
    from models.dish import Dish


class DishStorage:
    def __init__(self, db_session: 'DBSession', sql_data: dict[str, str]) -> None:
        self._db_session = db_session
        self._sql_data = sql_data
        self._init_table()
        # Временное хранилище в памяти
        self._dishes: dict[int, list[Dish]] = {}

    def _init_table(self) -> None:
        pass

    def save(self, dish: 'Dish') -> None:
        pass

    def load_by_id(self, id: int) -> Optional['Dish']:
        for dishes in self._dishes.values():
            for d in dishes:
                if d.id == id:
                    return d
        return None

    def load_by_category(self, category_id: int) -> List['Dish']:
        return self._dishes.get(category_id, [])

    def save_all(self, dishes: List['Dish']) -> None:
        """
        Добавляем несколько блюд по категориям
        """
        categories = {}
        for dish in dishes:
            if dish.category_id not in categories:
                categories[dish.category_id] = []
            categories[dish.category_id].append(dish)

        for category_id, dish_list in categories.items():
            if category_id in self._dishes:
                self._dishes[category_id].extend(dish_list)
            else:
                self._dishes[category_id] = dish_list