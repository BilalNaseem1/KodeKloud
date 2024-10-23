from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/post")
async def post():
    return {"data": "This is your post"}

# @app.post("/createpost")
# async def createpost(payload: dict = Body(...)):
#     print(payload)
#     return {"data": "This is your post"}

@app.post("/createpost")
async def createpost(payload: Post):
    print(payload)
    return {"data": "This is your post"}