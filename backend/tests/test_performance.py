import unittest
from unittest.mock import MagicMock, patch, ANY
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.api.cases import list_visa_cases

class TestCasesPerformance(unittest.IsolatedAsyncioTestCase):

    @patch("app.api.cases.supabase")
    @patch("app.api.cases.get_user_id_from_token")
    async def test_list_visa_cases_query_count(self, mock_get_user_id, mock_supabase):
        # Setup mock user
        mock_get_user_id.return_value = "user_123"

        # Setup mock query chain
        mock_table = MagicMock()
        mock_supabase.table.return_value = mock_table

        mock_query = MagicMock()
        mock_table.select.return_value = mock_query
        mock_query.eq.return_value = mock_query
        mock_query.range.return_value = mock_query
        mock_query.order.return_value = mock_query

        # Mock result
        mock_result = MagicMock()
        mock_result.data = [{
            "id": "case_1",
            "user_id": "user_123",
            "nationality": "India",
            "visa_type": "H-1B",
            "consulate": "Mumbai",
            "submission_date": "2023-01-01",
            "sponsor_type": "employer",
            "current_status": "pending",
            "created_at": "2023-01-01T00:00:00Z"
        }]
        mock_result.count = 10  # This should be populated if count='exact' was used
        mock_query.execute.return_value = mock_result

        # Call the function
        await list_visa_cases(page=1, per_page=10, authorization="Bearer token")

        # Check calls to select
        # Should now be only 1 call: select("*", count="exact")
        select_calls = mock_table.select.call_args_list
        print(f"Select calls: {select_calls}")

        # We expect exactly 1 call
        self.assertEqual(len(select_calls), 1, "Expected 1 select call (N+1 issue fixed)")

        # Check specifically for count="exact" in the first call
        first_call = select_calls[0]
        self.assertEqual(first_call.args[0], "*", "Expected select('*')")
        self.assertEqual(first_call.kwargs.get('count'), 'exact', "Expected count='exact'")

if __name__ == "__main__":
    unittest.main()
