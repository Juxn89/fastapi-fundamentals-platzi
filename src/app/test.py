from fastapi.testclient import TestClient

def test_client(client):
    assert type(client) == TestClient
    
def test_create_customer(client):
    response = client.post("/customers/", json={
        "name": "John Doe",
        "description": "This is a test customer",
        "email": "prueba@prueba.com",
        "age": 30
    })
    assert response.status_code == 200
    assert response.json()