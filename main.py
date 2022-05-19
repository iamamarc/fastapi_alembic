from fastapi import FastAPI
from api import users, courses, sections
from db.db_setup import engine
from models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and course.",
    version="0.0.1",
    contact={
        "name": "iamamarc",
        "email": ".....@.....",
    },
    license_info={
        "name": "MIT",
    },
    docs_url="/documentation", redoc_url="/",
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)