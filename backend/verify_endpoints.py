from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_cases():
    response = client.get("/api/cases")
    assert response.status_code == 200, f"Cases endpoint failed: {response.status_code}"
    data = response.json()
    assert "items" in data
    print(f"Cases endpoint OK. Total: {data.get('total')}")

def test_rules():
    response = client.get("/api/rules")
    assert response.status_code == 200, f"Rules endpoint failed: {response.status_code}"
    data = response.json()
    assert "items" in data
    print(f"Rules endpoint OK. Total: {data.get('total')}")

if __name__ == "__main__":
    test_cases()
    test_rules()
    print("All backend endpoints verified.")