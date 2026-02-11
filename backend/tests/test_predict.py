import pytest
from app.models.schemas import PredictionResult

def test_predict_status(client):
    response = client.post(
        "/api/predict/status",
        json={
            "case_id": "test_case_1",
            "case_data": {
                "nationality": "India",
                "visa_type": "H-1B",
                "consulate": "New Delhi",
                "submission_date": "2024-01-01",
            }
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "predicted_status" in data
    assert "approved" in data["predicted_status"]

def test_predict_processing_time(client):
    response = client.post(
        "/api/predict/processing-time",
        json={
            "case_id": "test_case_2",
            "case_data": {
                "nationality": "China",
                "visa_type": "F-1",
            }
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "estimated_days_remaining" in data

def test_explain_prediction(client):
    response = client.get("/api/predict/explain/test_case_3")
    assert response.status_code == 200
    data = response.json()
    assert "top_factors" in data
