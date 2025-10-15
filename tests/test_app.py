from app import app


def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert "Welcome" in response.get_json()["message"]


def test_create_user():
    client = app.test_client()
    data = {"name": "Kiran", "email": "kiran@example.com"}
    response = client.post('/user', json=data)
    assert response.status_code == 201
    res_json = response.get_json()
    assert res_json["status"] == "User created successfully"
    assert res_json["user"]["name"] == "Kiran"
