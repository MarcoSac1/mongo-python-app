from app.repositories.base_repository import BaseRepository


class CourseRepository(BaseRepository):

    def __init__(self):
        super().__init__("courses")

    def get_by_category(self, category: str):
        return self.find_many({"category": category})
