from pymongo import MongoClient
from pymongo.server_api import ServerApi

from app.config import settings


class MongoDatabase:
    _client = None
    _database = None
    
    @classmethod
    def connect(cls):
        if cls._client is None:
            if settings.MONGO_URI is None or settings.MONGO_DB_NAME is None:
                raise ValueError(
                    "MONGO_URI e MONGO_DB_NAME devono essere impostati nelle variabili d'ambiente"
                )

            if settings.MONGO_URI.startswith("mongodb+srv://"):
                cls._client = MongoClient(
                    settings.MONGO_URI,
                    server_api=ServerApi("1")
                )
            else:
                cls._client = MongoClient(settings.MONGO_URI)

            cls._database = cls._client[settings.MONGO_DB_NAME]
            cls._client.admin.command("ping")
            print("Connessione a MongoDB riuscita")
            
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
    