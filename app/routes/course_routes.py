from fastapi import APIRouter, HTTPException

from app.models.course_model import CourseCreate, CourseUpdate
from app.repositories.course_repository import CourseRepository

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

course_repository = CourseRepository()


@router.get("")
def get_courses():
    courses = course_repository.get_all()
    return {
        "count": len(courses),
        "data": courses
    }


@router.get("/{course_id}")
def get_course_by_id(course_id: str):
    course = course_repository.get_by_id(course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Corso non trovato")
    return course


@router.post("")
def create_course(course: CourseCreate):
    course_data = course.model_dump()
    return course_repository.create(course_data)


@router.put("/{course_id}")
def update_course(course_id: str, course: CourseUpdate):
    course_data = course.model_dump(exclude_none=True)
    updated_course = course_repository.update(course_id, course_data)
    if updated_course is None:
        raise HTTPException(status_code=404, detail="Corso non trovato")
    return updated_course


@router.delete("/{course_id}")
def delete_course(course_id: str):
    deleted = course_repository.delete(course_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Corso non trovato")
    return {
        "message": "Corso eliminato correttamente"
    }


@router.get("/search/category/{category}")
def search_courses_by_category(category: str):
    courses = course_repository.get_by_category(category)
    return {
        "count": len(courses),
        "data": courses
    }
