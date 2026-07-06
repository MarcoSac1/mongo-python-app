from fastapi import APIRouter, HTTPException
from app.repositories.grade_repository import GradeRepository

router = APIRouter(
    prefix="/grades",
    tags=["Grades - Read"]
)

grade_repository = GradeRepository()

@router.get("")
def get_grades():
    grades = grade_repository.get_all()
    return {"count": len(grades), "data": grades}

@router.get("/{grade_id}")
def get_grade_by_id(grade_id: str):
    grade = grade_repository.get_by_id(grade_id)
    if grade is None:
        raise HTTPException(status_code=404, detail="Voto non trovato")
    return grade

@router.get("/student/{student_id}")
def get_grades_by_student(student_id: str):
    grades = grade_repository.get_by_student(student_id)
    return {"count": len(grades), "data": grades}

@router.get("/student/{student_id}/average")
def get_student_average(student_id: str):
    grades = grade_repository.get_by_student(student_id)
    if not grades:
        return {"student_id": student_id, "average": None, "message": "Nessun voto trovato"}
    media = sum(g["value"] for g in grades) / len(grades)
    return {"student_id": student_id, "average": round(media, 2), "count": len(grades)}
