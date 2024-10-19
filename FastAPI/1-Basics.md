# Venv Basics
```bash
python3 -m venv <venv-name>
source venv/bin/activate            #enable venv for terminal
```
### Change interpretor:
`view` -> `command pallete` -> `python select interpretor` -> `enter inerpretor path` -> `./venv/bin/python`

```
pip install fastapi
pip freeze

pip install uvicorn
```

### main.py
```python
from fastapi import FastAPI

app = FastAPI()

# path operation
@app.get("/")       # this decorator converts this function to a path operation in the url to access
async def root():
    return {"message": "Hello World"}

@app.get("/post")
async def post():
    return {"data": "This is your post"}
```

### Starting the web server
```bash
uvicorn <file-name>:<fast-api-instance>
uvicorn main:app
```


## Postman
To test an api we dont need to build an entire front end for it. Postman is used for testing APIs. It allows to construct http requests.

![alt text](image-1.png)

![alt text](image.png)

##  Post requests
with post request we can send data to the api server - for creating things.

```python
@app.post("/createpost")
async def createpost():
    return {"data": "This is your post"}
```