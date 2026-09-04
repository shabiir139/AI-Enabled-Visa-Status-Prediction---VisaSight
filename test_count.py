from supabase import create_client, Client
import os
from unittest.mock import MagicMock

print("In backend API we have dual query pattern.")
print("Query 1: select('*')")
print("Query 2: select('id', count='exact')")
print("We can combine this to single query: select('*', count='exact')")
