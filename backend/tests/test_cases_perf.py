import pytest
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
import sys
import os

# Add backend directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.api.cases import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router, prefix="/api/cases")

client = TestClient(app)

def test_list_visa_cases_query_optimization():
    # Setup mock data
    mock_data = [{
        "id": "1",
        "user_id": "test_user",
        "nationality": "US",
        "visa_type": "H-1B",
        "consulate": "London",
        "submission_date": "2023-01-01",
        "sponsor_type": "employer",
        "current_status": "pending",
        "created_at": "2023-01-01T00:00:00Z"
    }]

    with patch("app.api.cases.supabase") as mock_supabase:
        # Setup the mock chain
        mock_table = mock_supabase.table.return_value
        mock_select = mock_table.select.return_value
        mock_eq = mock_select.eq.return_value
        mock_range = mock_eq.range.return_value
        mock_order = mock_range.order.return_value

        # Configure the return value for the data query
        mock_result = MagicMock()
        mock_result.data = mock_data
        # This count is for the optimized version where count is returned with data
        mock_result.count = 1

        mock_order.execute.return_value = mock_result

        # We also need to handle the unoptimized path which does a second query
        # The second query is: supabase.table("visa_cases").select("id", count="exact").eq(...).execute()

        # For the unoptimized path, the first execute returns data but maybe not count
        # And there is a second chain.

        # Let's just make all execute calls return the same mock_result for simplicity
        # The test is checking call counts, not data correctness primarily.

        # Mock the second query chain for the unoptimized version
        mock_count_select = mock_table.select.return_value
        mock_count_eq = mock_count_select.eq.return_value
        mock_count_eq.execute.return_value = mock_result

        # Mock user authentication
        with patch("app.api.cases.get_user_id_from_token", return_value="test_user"):
             response = client.get("/api/cases")

        assert response.status_code == 200

        # Check how many times table() was called.
        # Unoptimized: called twice (once for data, once for count)
        # Optimized: called once
        print(f"Supabase table call count: {mock_supabase.table.call_count}")

        if mock_supabase.table.call_count > 1:
            pytest.fail(f"Performance Regression: supabase.table() called {mock_supabase.table.call_count} times. Expected 1 time.")
