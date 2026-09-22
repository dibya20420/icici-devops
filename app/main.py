from fastapi import FastAPI

app=FastAPI()

@app.get("/home")
def home():
    return {"message","welcome HOme"}


@app.get("/login")
def login():
    return {"message","welcome to login page"}