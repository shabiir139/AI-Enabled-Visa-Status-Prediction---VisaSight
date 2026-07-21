import sys
from unittest.mock import MagicMock

# Mock fastapi and schemas
sys.modules['fastapi'] = MagicMock()
sys.modules['app.models.schemas'] = MagicMock()
sys.modules['app.db.supabase'] = MagicMock()

# Now try importing the rules API
try:
    from backend.app.api.rules import list_visa_rules
    print("Imports successful.")
except Exception as e:
    print(f"Error: {e}")
