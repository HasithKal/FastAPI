from fastapi import FastAPI,Path,Response,status,HTTPException
from typing import Annotated
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
app = FastAPI()
class Post(BaseModel):
    Title:str
    Content:str

my_posts=[{"title":"Title of post 1","content":"Content of post 1","id":1},{"title":"Title of post 2","content":"Content of post 2","id":2}]
@app.get("/")
def read_root():
    return {"data":my_posts}

def find_post(id):
    for i,p in enumerate(my_posts):
        if(p['id']==id):
            return i
@app.post("/createposts",status_code=201)
def post(new_post:Post):
    post_dict=new_post.dict()
    post_dict['id']=randrange(0,10000000)
    my_posts.append(post_dict)
    return {"data":new_post}

@app.get("/get_post/{id}")
def get_post(id:Annotated[int,Path(ge=1)],response:Response):
    for i in my_posts:
        if(i['id']==id):
            return i
    # response.status_code=404
    # return {'message':'id not found'}
    raise HTTPException(status_code=404,detail='Id not found')
    
@app.delete("/delete_post/{id}",status_code=204)
def delete_post(id:int):
    index=find_post(id)
    my_posts.pop(index)
    return {'message':'post was successfully deleted'}

