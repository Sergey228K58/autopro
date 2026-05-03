def login_admin(client):
    client.post("/login", data={"username": "admin", "password": "admin"})


def test_client_portal_access_for_admin(client):
    login_admin(client)
    response = client.get("/client-portal", follow_redirects=True)

    assert response.status_code == 200
    assert "AutoPro" in response.text
