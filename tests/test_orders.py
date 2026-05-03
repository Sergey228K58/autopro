def login_admin(client):
    client.post("/login", data={"username": "admin", "password": "admin"})


def test_create_order(client):
    login_admin(client)

    response = client.post("/orders/create", data={
        "client_name": "Иван",
        "client_username": "ivan123",
        "car_brand": "Toyota",
        "car_model": "Camry",
        "year": "2020",
        "config": "Comfort",
        "color": "Black",
        "price": "2500000"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Toyota" in response.data
