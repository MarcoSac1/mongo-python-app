from pymongo import ASCENDING

from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__("users")
        self.create_indexes()

    def create_indexes(self):
        self.collection.create_index(
            [("email", ASCENDING)],
            unique=True
        )

    def get_by_email(self, email: str):
        return self.find_one({"email": email})

    def get_active_users(self):
        return self.find_many({"active": True})

    def search_by_city(self, city: str):
        return self.find_many({"city": city})