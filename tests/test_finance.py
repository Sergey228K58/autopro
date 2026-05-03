def login_admin(client):
    client.post("/login", data={"username": "admin", "password": "admin"})


def test_finance_add(client):
    login_admin(client)

    response = client.post("/finance/add", data={
        "type": "доход",
        "category": "Продажа авто",
        "amount": "1000000",
        "related_order_id": ""
    }, follow_redirects=True)

    assert response.status_code == 200
