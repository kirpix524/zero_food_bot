from typing import List, Optional

from models.dish import Dish


class DishRepository:
    def __init__(self) -> None:
        pass

    def get_by_category(self, category_id: int) -> List[Dish]:
        pass
    def get_by_id(self, id: int) -> Optional[Dish]:
        pass
    def create_bulk(self, dishes: List[Dish]) -> None:
        pass