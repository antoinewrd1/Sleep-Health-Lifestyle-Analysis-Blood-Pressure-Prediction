from fastapi.testclient import TestClient

from src.api.main import app


client = TestClient(app)


def test_health_route_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_predict_route_returns_prediction():
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


def test_schema_drift_route_detects_missing_column():
    payload = {
        "reference_columns": ["Age", "Stress Level"],
        "current_columns": ["Age"],
    }

    response = client.post("/monitoring/schema-drift", json=payload)

    assert response.status_code == 200
    assert response.json()["missing_columns"] == ["Stress Level"]