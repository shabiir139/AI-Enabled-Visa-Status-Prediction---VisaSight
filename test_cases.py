import sys
import unittest.mock as mock

sys.modules['fastapi'] = mock.MagicMock()

from app.api.cases import list_visa_cases

print("Backend imports successfully")
