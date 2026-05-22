from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"status": "online", "message": "這是簡易計算機 API"}


@app.get("/add")
def calculate_add(a: float, b: float):
    result = add_func(a, b)
    return {"status": "addition", "a": a, "b": b, "result": result}


def add_func(a: float, b: float) -> float:
    return a + b


def sub_func(a, b):
    # temp = 123
    return a - b


def mut_func(a: float, b: float) -> float:
    # return "123"
    return a * b
