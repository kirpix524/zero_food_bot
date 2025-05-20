from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.feedback import Feedback
    from storage.feedback_storage import FeedbackStorage

class FeedbackRepository:
    def __init__(self, storage: 'FeedbackStorage'):
        self._storage = storage

    def create(self, feedback: 'Feedback') -> None:
        pass

    def get_latest(self, n: int) -> List['Feedback']:
        pass