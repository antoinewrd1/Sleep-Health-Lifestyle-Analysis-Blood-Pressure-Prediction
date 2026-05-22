from fastapi.testclient import TestClient

from src.api.main import app


client = TestClient(app)


def test_root_endpoint_returns_status_message():
    response = client.get("/")

    assert response.status_code == 200
    assert "message" in response.json()


def test_predict_endpoint_returns_prediction():
    payload = {
        "age": 40,
        "sleep_duration": 7.0,
        "quality_of_sleep": 7,
        "physical_activity_level": 50,
        "stress_level": 5,
        "heart_rate": 75,
        "daily_steps": 7000,
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert "predicted_systolic_bp" in response.json()