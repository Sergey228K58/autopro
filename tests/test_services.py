def login_master(client):
    client.post("/login", data={"username": "admin", "password": "admin"})


def test_create_service_order(client):
    login_master(client)

    response = client.post("/service/create", data={
        "client_username": "ivan123",
        "vin": "123456789",
        "works": "Замена масла",
        "hours": "1.5",
        "work_cost": "3000",
        "parts_cost": "1500"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"service" in response.data
