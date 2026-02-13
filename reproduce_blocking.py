import time
import requests
import threading
import sys
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "http://localhost:8080"

def check_health():
    start = time.time()
    try:
        response = requests.get(f"{BASE_URL}/health")
        duration = time.time() - start
        print(f"Health check status: {response.status_code}, duration: {duration:.4f}s")
        return duration
    except Exception as e:
        print(f"Health check failed: {e}")
        return 999

def trigger_prediction():
    start = time.time()
    try:
        data = {
            "case_id": "test-123",
            "case_data": {
                "nationality": "India",
                "visa_type": "H-1B"
            }
        }
        print("Triggering prediction...")
        response = requests.post(f"{BASE_URL}/api/predict/status", json=data)
        duration = time.time() - start
        print(f"Prediction status: {response.status_code}, duration: {duration:.4f}s")
    except Exception as e:
        print(f"Prediction failed: {e}")

def main():
    # Wait for server to be ready
    print("Waiting for server...")
    for _ in range(10):
        try:
            if requests.get(f"{BASE_URL}/health").status_code == 200:
                print("Server is ready.")
                break
        except:
            time.sleep(1)
    else:
        print("Server failed to start.")
        sys.exit(1)

    print("\n--- Starting Blocking Test ---")

    # Start prediction in a separate thread
    executor = ThreadPoolExecutor(max_workers=2)

    # Submit prediction
    future_pred = executor.submit(trigger_prediction)

    # Wait a tiny bit to ensure prediction request has reached the server and started processing
    time.sleep(0.5)

    # Check health while prediction is processing
    print("Checking health during prediction...")
    duration = check_health()

    if duration > 1.0:
        print("\n❌ FAILURE: Health check was blocked! It took > 1.0s")
    else:
        print("\n✅ SUCCESS: Health check was NOT blocked! It took < 1.0s")

if __name__ == "__main__":
    main()
