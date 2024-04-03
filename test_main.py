from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_sensor():
    sensor_id = 1
    response = client.get(f"/sensors/{sensor_id}")
    assert response.status_code == 200
    # Предположим, что ответ содержит JSON с деталями сенсора
    assert "sensor_name" in response.json()
    assert "sensor_id" in response.json()


def test_read_measurements_type():
    type_id = 1
    response = client.get(f"/measurement_types/{type_id}")
    assert response.status_code == 200
    # Проверяем, что в ответе есть информация о типе измерения
    assert "type_name" in response.json()
    assert "type_units" in response.json()


def test_create_measurements_type():
    response = client.post(
        "/measurement_types/",
        json={"type_name": "Temperature", "type_units": "&"},
    )
    assert response.status_code == 200
    assert response.json()["type_name"] == "Temperature"
    assert response.json()["type_units"].strip() == "&"


