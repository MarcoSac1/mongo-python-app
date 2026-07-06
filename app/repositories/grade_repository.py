from app.repositories.base_repository import BaseRepository

class GradeRepository(BaseRepository):
    def __init__(self):
        super().__init__("grades")

    def get_by_student(self, student_id: str):
        return self.find_many({"student_id": student_id})

    def get_by_subject(self, subject: str):
        return self.find_many({"subject": subject})