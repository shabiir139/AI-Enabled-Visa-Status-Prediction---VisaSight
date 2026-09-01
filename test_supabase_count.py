import sys
import os

try:
    from supabase import create_client
    print("Supabase imported successfully")
except Exception as e:
    print(f"Error importing supabase: {e}")
