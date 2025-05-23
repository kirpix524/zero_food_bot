from typing import List, Optional, TYPE_CHECKING



if TYPE_CHECKING:
    from models.category import Category
    from storage.category_storage import CategoryStorage


class CategoryRepository:
    def __init__(self, storage: 'CategoryStorage') -> None:
        self._storage: 'CategoryStorage' = storage
        self._categories: List['Category'] = self._storage.load_all()

    def get_all(self) -> List['Category']:
        return self._storage.load_all()

    def get_by_id(self, id: int) -> Optional['Category']:
        pass

    def create(self, category: 'Category') -> None:
        pass

    def del_all(self) -> None:
        pass