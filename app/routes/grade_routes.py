from fastapi import APIRouter, HTTPException
from app.repositories.grade_repository import GradeRepository
from app.models.grade_model import GradeCreate, GradeUpdate

router = APIRouter(
    prefix="/grades",
    tags=["Grades"]
)

grade_repository = GradeRepository()

@router.post("")
def create_grade(grade: GradeCreate):
    grade_data = grade.model_dump()
    return grade_repository.create(grade_data)

@router.put("/{grade_id}")
def update_grade(grade_id: str, grade: GradeUpdate):
    grade_data = grade.model_dump(exclude_none=True)
    updated = grade_repository.update(grade_id, grade_data)
    if updated is None:
        raise HTTPException(status_code=404, detail="Voto non trovato")
    return updated

@router.delete("/{grade_id}")
def delete_grade(grade_id: str):
    deleted = grade_repository.delete(grade_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Voto non trovato")
    return {"message": "Voto eliminato correttamente"}