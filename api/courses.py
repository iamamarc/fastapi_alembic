from fastapi import APIRouter, Depends

from db.db_setup import get_db

router = APIRouter()


@router.get("/courses")
async def read_courses(db: Session = Depends(get_db)):
    courses = get_course(db=db)
    return courses

@router.post("/courses")
async def create_course_api():
    return {"courses": []}


@router.get("/courses/{id}")
async def read_courses():
    return {"courses": []}


@router.patch("/courses/{id}")
async def update_course():
    return {"courses": []}


@router.delete("/courses/{id}")
async def delete_course():
    return {"courses": []}


@router.get("/courses/{id}/sections")
async def read_course_sections():
    return {"courses": []}
