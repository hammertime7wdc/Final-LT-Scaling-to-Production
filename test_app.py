from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert b"Goodbye, World!" in response.data  
    assert b"Hello, World!" in response.data