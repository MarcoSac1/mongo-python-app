from fastapi import FastAPI
from app.database import MongoDatabase
from app.routes.user_routes import router as user_router
from app.routes.course_routes import router as course_router

app = FastAPI(
    title="MongoDB Atlas Python API",
    description="API modulare con FastAPI, PyMongo e MongoDB Atlas",
    version="1.0.0"
)

app.include_router(user_router)
app.include_router(course_router)

@app.get("/")
def home():
    return {
        "message": "API collegata a MongoDB Atlas"
    }

@app.on_event("shutdown")
def shutdown_event():
    MongoDatabase.close_connection()
