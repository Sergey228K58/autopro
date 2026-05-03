def test_login_success(client):
    response = client.post("/login", data={
        "username": "admin",
        "password": "admin"
    }, follow_redirects=True)

    assert "Главная" in response.text or "index" in response.text


def test_login_fail(client):
    response = client.post("/login", data={
        "username": "admin",
        "password": "wrong"
    })

    assert "Неверный логин" in response.text
