from app.repositories.user_repository import UserRepository
from app.database import MongoDatabase

user_repository = UserRepository()
new_user = user_repository.create({
    "name": "Mario",
    "surname": "Rossi",
    "email": "mario.rossi@example.com",
    "city": "Catania",
    "active": True
    })

print("Utente creato:")
print(new_user)

users = user_repository.get_all()
print("Lista utenti:")

print(users)

MongoDatabase.close_connection()