from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    id: int = None
    published: bool = False

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World!"}

@app.post("/hello")
def hello_post(post: Post):
    return post

client = TestClient(app)

#def test_hello():
#    response = client.get("/")
#    assert response.status_code == 200

def test_post():
    response = client.post("/hello", json = {"title": "my title", "id": 1, "published": False})
    print("response", response.json())


#We define our appliction endpoints using get, post, put and delete method as usual. In this case, we will use pydantic to validate the data type. 

#Then we define testclient to behave as server and by passing to method same as endpoints, we can see if they are matching with expected results.

#In case of post, we need to define the body as well. 


