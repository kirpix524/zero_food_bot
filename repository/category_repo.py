from typing import List, Optional

from models.category import Category

class CategoryRepository:
    def __init__(self) -> None:
        pass

    def get_all(self) -> List[Category]:
        pass

    def get_by_id(self, id: int) -> Optional[Category]:
        pass

    def create(self, category: Category) -> None:
        pass

    def delete_all(self) -> None:
        pass