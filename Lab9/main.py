from fastapi import FastAPI
from database import Base, engine
from routes.user_routes import router as user_router
from routes.post_routes import router as post_router

# Инициализация приложения
app = FastAPI()

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Подключение маршрутов
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(post_router, prefix="/posts", tags=["Posts"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# uvicorn main:app --reload
# http://127.0.0.1:8000/docs