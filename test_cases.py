import asyncio
from unittest.mock import MagicMock, patch

from app.api.cases import list_visa_cases

class MockResult:
    def __init__(self, data, count=None):
        self.data = data
        self.count = count

@patch("app.api.cases.supabase")
def test_list_cases(mock_supabase):
    mock_query = MagicMock()
    mock_supabase.table.return_value.select.return_value = mock_query
    mock_query.eq.return_value = mock_query
    mock_query.range.return_value = mock_query
    mock_query.order.return_value = mock_query

    mock_data = [
        {
            "id": "1", "user_id": "test_user", "nationality": "India",
            "visa_type": "H-1B", "consulate": "Mumbai", "submission_date": "2023-01-01",
            "documents_submitted": [], "sponsor_type": "employer",
            "prior_travel": False, "current_status": "pending", "created_at": "2023-01-01T00:00:00"
        }
    ]
    mock_query.execute.return_value = MockResult(data=mock_data, count=100)

    response = asyncio.run(list_visa_cases(page=1, per_page=10, authorization="Bearer test_token"))

    # Check that we got the mocked structure correctly
    assert response.total == 100
    assert len(response.items) == 1
    assert response.items[0].id == "1"
    assert response.total_pages == 10

    print("Test passed for list_visa_cases!")

test_list_cases()
