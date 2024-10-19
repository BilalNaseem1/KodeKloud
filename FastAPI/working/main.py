from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/post")
async def post():
    return {"data": "This is your post"}

@app.post("/createpost")
async def createpost():
    return {"data": "This is your post"}