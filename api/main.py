from fastapi import FastAPI
from model.user_connection import UserConnection

app = FastAPI()
conn = UserConnection

@app.get("/")
def root():
    conn
    return "Hi, I am FastAPI"

