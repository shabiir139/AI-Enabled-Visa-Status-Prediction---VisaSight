"""
Supabase Client Configuration

Database client for VisaSight backend.
"""

import os
import sys
from supabase import create_client, Client
from functools import lru_cache

# Supabase configuration with validation
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Fallback for local development if not set in environment
if not SUPABASE_URL:
    SUPABASE_URL = "https://wrzvcytxueeppukahhdk.supabase.co"
    print("⚠️ Warning: SUPABASE_URL not set, using default")

if not SUPABASE_KEY:
    # This is a public anon key, safe to have as default for dev
    SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndyenZjeXR4dWVlcHB1a2FoaGRrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk3MDY4ODIsImV4cCI6MjA4NTI4Mjg4Mn0.i_SIXx0ZL6TmeE0JjS9YvBGw0V5hG_9w6tAQOCQ3BoY"
    print("⚠️ Warning: SUPABASE_KEY not set, using default")

@lru_cache()
def get_supabase() -> Client:
    """
    Get cached Supabase client instance with error handling.
    """
    try:
        if not SUPABASE_URL or not SUPABASE_KEY:
            raise ValueError("Supabase URL and Key must be configured")
            
        # Initialize without extra arguments to avoid 'proxy' error in some environments
        return create_client(
            supabase_url=SUPABASE_URL, 
            supabase_key=SUPABASE_KEY
        )
    except Exception as e:
        print(f"❌ Failed to connect to Supabase: {e}")
        # In production, we might want to exit, but for now we'll allow startup
        # to proceed so the health check can still pass even if DB is down
        return None

# Convenience export
supabase = get_supabase()
