from pymongo import MongoClient
from pymongo.server_api import ServerApi

from app.config import settings


class MongoDatabase:
    _client = None
    _database = None
    
    @classmethod
    def  connect(cls):
        if cls._client is None:
            cls._client = MongoClient(
                settings.MONGO_URI,
                server_api = ServerApi("1")
            )
            
            cls._database = cls._client[settings.MONGO_DB_NAME]
            
            cls._client.admin.command("ping")
            print("Connessione a MongoDB Atlas riuscita")
            
        return cls._database
    
    @classmethod
    def get_database(cls):
        if cls._database is None:
            return cls.connect()
        
        return cls._database
    
    @classmethod
    def close_connection(cls):
        if cls._client is not None:
            cls._client.close()
            cls._client = None
            cls._database = None
            print("Connessione a MangoDB chiusa")
    