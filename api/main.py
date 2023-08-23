from fastapi import FastAPI
from model.user_connection import UserConnection

app = FastAPI()
conn = UserConnection

@app.get("/")
def root():
    conn
    return "Hi, I am FastAPI"

@app.get("/{country}")
def get_publications_by_country(country: str):
    publications = {}
    for data in conn.read_publications_by_country(country):
        item = {}
        item["publication_id"] = data[0]
        item["publication_date"] = data[1]
        item["pub_type"] = data[2]
        item["city"] = data[3]
        item["address"] = data[4]
        item["image_publication_id"] = data[5]
        item["pet_id"] = data[6]
        item["user_id"] = data[7]
        publications.append(item)
    return publications
