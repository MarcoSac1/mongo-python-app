from fastapi import APIRouter, HTTPException
from pymongo.errors import DuplicateKeyError

from app.repositories.user_repository import UserRepository 
from app.models.user_model import UserCreate, UserUpdate


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

user_repository = UserRepository()

@router.get("")
def get_users():
    users = user_repository.get_all()
    return {
        "count": len(users),
        "data": users
    }


@router.get("/{user_id}")
def get_user_by_id(user_id: str):
    user = user_repository.get_by_id(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="Utente non trovato")


    return user

@router.post("")
def create_user(user: UserCreate):
    try: 
        user_data = user.model_dump()
        return user_repository.create(user_data)
    except DuplicateKeyError:
        raise HTTPException(
            status_code=400,
            detail="Esiste gia un utente con questa mail"
        )

@router.put("/{user_id}")
def update_user(user_id: str, user: UserUpdate):
    user_data = user.model_dump(exclude_none=True)
    updated_user = user_repository.update(user_id, user_data)

    if updated_user is None:
        raise HTTPException(status_code=404, detail="Utente non trovato")
    return updated_user


@router.get("/search/city/{city}")
def search_user_by_city(city: str):
    users = user_repository.search_by_city(city) 

    return {
        "count": len(users),
        "data": users
    }  

@router.delete("/{user_id}")
def delete_user(user_id: str):
    deleted = user_repository.delete(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Utente non trovato")
    return {"message": "Utente eliminato"}