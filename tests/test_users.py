from app import schemas
from app.config import settings
from jose import jwt
import pytest


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_create_user(client):
    response = client.post(
        "/users/",
        json={"email": "testing1@example.com", "password": "password123"},
    )
    assert response.status_code == 201
    assert response.json()["email"] == "testing1@example.com"


def test_login_error(test_user, client):
    response = client.post(
        "/login",
        data={"username": test_user['email'],
              "password": test_user['password']},
    )
    login_res = schemas.Token(**response.json())
    payload = jwt.decode(login_res.access_token,
                         settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert login_res.token_type == "bearer"
    assert id == test_user['id']
    assert response.status_code == 200


@pytest.mark.parametrize("email, password, expected_status", [
    ('wrongemail@gmail.com', 'password123', 403),
    ('testing1@gmail.com', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, 'password123', 403),
    ('testing1@gmail.com', None, 403)])
def test_failed_login(client, test_user, email, password, expected_status):
    response = client.post(
        "/login",
        data={"username": email, "password": password}
    )
    assert response.status_code == expected_status
    # assert response.json().get("detail") == "Invalid credentials"
