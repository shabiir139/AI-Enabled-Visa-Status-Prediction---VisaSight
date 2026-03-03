import asyncio
from unittest.mock import MagicMock, patch

from app.api.rules import list_visa_rules

class MockResult:
    def __init__(self, data, count=None):
        self.data = data
        self.count = count

@patch("app.api.rules.supabase")
def test_list_rules(mock_supabase):
    mock_query = MagicMock()
    # The chain is supabase.table("visa_rules").select("*", count="exact").eq("is_active", True)
    mock_supabase.table.return_value.select.return_value.eq.return_value = mock_query
    mock_query.eq.return_value = mock_query
    mock_query.range.return_value = mock_query
    mock_query.order.return_value = mock_query

    mock_data = [
        {
            "id": "r1", "country": "USA", "visa_type": "H-1B",
            "rule_category": "eligibility", "title": "Test Rule",
            "description": "Test Desc", "effective_date": "2023-01-01",
            "source_url": "http://test.com", "created_at": "2023-01-01T00:00:00"
        }
    ]
    mock_query.execute.return_value = MockResult(data=mock_data, count=50)

    response = asyncio.run(list_visa_rules(page=2, per_page=10))

    # Check that we got the mocked structure correctly
    assert response.total == 50
    assert len(response.items) == 1
    assert response.items[0].id == "r1"
    assert response.total_pages == 5

    print("Test passed for list_visa_rules!")

test_list_rules()
