from fastapi import APIRouter

from app.repositories.course_repository import CourseRepository
from app.models.course_model import CourseCreate


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


@router.post("")
def create_course(course: CourseCreate):
    course_data = course.model_dump()

    return course_repository.create(course_data)
