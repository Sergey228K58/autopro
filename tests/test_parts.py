def login_storekeeper(client):
    client.post("/login", data={"username": "admin", "password": "admin"})


def test_receive_parts(client):
    login_storekeeper(client)

    response = client.post("/parts/receive", data={
        "name": "Фильтр",
        "article": "FLT123",
        "category": "Двигатель",
        "supplier": "Bosch",
        "qty": "10",
        "min_qty": "2",
        "price": "500"
    }, follow_redirects=True)

    assert "Фильтр" in response.text or "parts" in response.text
