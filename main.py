from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    Title:str
    Content:str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/createposts")
def post(new_post:Post):
    print(new_post)
    print(new_post.dict())
    return {"Title":new_post.dict()}

