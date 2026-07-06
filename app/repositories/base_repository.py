from app.database import MongoDatabase
from app.utils.mongo_helpers import serialize_document, serialize_documents, to_object_id


class BaseRepository:
    def __init__(self, collection_name: str):
        db = MongoDatabase.get_database()
        self.collection = db[collection_name]

    def get_all(self, filters: dict = None, limit: int = 100, skip: int = 0, sort: list = None):
        filters = filters or {}
        sort = sort or [("_id", -1)]
        cursor = (
            self.collection
            .find(filters)
            .sort(sort)
            .skip(skip)
            .limit(limit)
        )
        return serialize_documents(list(cursor))

    def get_by_id(self, id_value: str):
        object_id = to_object_id(id_value)
        if object_id is None:
            return None
        document = self.collection.find_one({"_id": object_id})
        return serialize_document(document)

    def create(self, data: dict):
        result = self.collection.insert_one(data)
        return self.get_by_id(str(result.inserted_id))

    def update(self, id_value: str, data: dict):
        object_id = to_object_id(id_value)
        if object_id is None:
            return None
        self.collection.update_one(
            {"_id": object_id},
            {"$set": data}
        )
        return self.get_by_id(id_value)

    def delete(self, id_value: str):
        object_id = to_object_id(id_value)
        if object_id is None:
            return False
        result = self.collection.delete_one({"_id": object_id})
        return result.deleted_count > 0

    def find_one(self, filters: dict):
        document = self.collection.find_one(filters)
        return serialize_document(document)

    def find_many(self, filters: dict, limit: int = 100, skip: int = 0):
        cursor = (
            self.collection
            .find(filters)
            .skip(skip)
            .limit(limit)
        )
        return serialize_documents(list(cursor))

    def count(self, filters: dict = None):
        filters = filters or {}
        return self.collection.count_documents(filters)
