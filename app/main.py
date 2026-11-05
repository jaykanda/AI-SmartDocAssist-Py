import os
from dotenv import load_dotenv
from fastapi import FastAPI

# load the env variables from the local .env file
load_dotenv()
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}