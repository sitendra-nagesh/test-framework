from fastapi import FastAPI
from fastapi.testclient import TestClient
app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello World!"}

client = TestClient(app)

def test_hello_world():
    response = client.get("/")
    print("response", response.status_code)
    print("response_type", type(response))
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}


# steps to run code
# pytest -v -s main.py

# testclient will allow to test your code without deploying it.

