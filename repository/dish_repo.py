# repository/dish_repo.py

from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from storage.dish_storage import DishStorage
    from models.dish import Dish

class DishRepository:
    def __init__(self, storage: 'DishStorage') -> None:
        self._storage: 'DishStorage' = storage

    def get_by_category(self, category_id: int) -> List['Dish']:
        return self._storage.load_by_category(category_id)

    def get_by_id(self, id: int) -> Optional['Dish']:
        return self._storage.load_by_id(id)

    def create_bulk(self, dishes: List['Dish']) -> None:
        self._storage.save_all(dishes)


class DishRepo:
    @staticmethod
    def initialize(storage: 'DishStorage'):
        """
        Временная загрузка тестовых данных
        """
        test_dishes = [
            Dish(
                id=1,
                category_id=1,
                name="Греческий салат «Афины»",
                short_description="Освежающий микс овощей с брынзой и оливками",
                description="Хрустящие огурцы и помидоры, сочный болгарский перец...",
                price=450,
                photo_url="images/salads/Greek salad Athens/01.png"
            ),
            Dish(
                id=2,
                category_id=1,
                name="Салат с печёной свёклой и козьим сыром",
                short_description="Нежная свёкла и пикантный сыр на подушке рукколы",
                description="Запечённая до карамелизации свёкла на свежей рукколе...",
                price=520,
                photo_url="images/salads/Salad with roasted beetroot and goat's cheese/01.png"
            )
        ]
        repo = DishRepository(storage)
        repo.create_bulk(test_dishes)