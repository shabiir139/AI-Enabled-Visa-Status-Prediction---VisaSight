from app.db.supabase import supabase

def test_query():
    try:
        result = supabase.table("visa_cases").select("*", count="exact").range(0, 9).execute()
        print(f"Data length: {len(result.data)}")
        if hasattr(result, 'count'):
            print(f"Count: {result.count}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_query()
