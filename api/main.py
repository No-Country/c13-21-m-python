from fastapi import FastAPI
from model.user_connection import UserConnection
from schema.user_schema import UserSchema

app = FastAPI()
conn = UserConnection

@app.get("/")
def root():
    conn
    return "Hi, I am FastAPI"

@app.post("/api/user")
def insert(user_data:UserSchema):
    data = user_data.dict()
    data.pop("user_id")
    conn.write(data)
