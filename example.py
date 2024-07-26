from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def get_root():
    return {"Hello, World!"}

@app.get("/item/{id}")
def get_item(id: int):
    return {"item": id * 2}
