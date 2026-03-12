from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User, UserAge, Feedback

my_app = FastAPI()

feedbacks = []

@my_app.get("/")
def read_root():
    return FileResponse("index.html")


@my_app.post("/calculate")
def calculate(num1: int, num2: int):
    result = num1 + num2
    return {"result": result}

user = User(
    name="Иван Яковлев",
    id=1
)

@my_app.get("/users")
def get_user():
    return user

@my_app.post("/user")
def create_user(user: UserAge):
    is_adult = user.age >= 18

    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

@my_app.post("/feedback")
def create_feedback(feedback: Feedback):
    feedbacks.append(feedback)

    return {
        "message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."
    }