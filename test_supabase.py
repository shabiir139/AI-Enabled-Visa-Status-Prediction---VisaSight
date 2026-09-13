import asyncio
from app.db.supabase import supabase

async def main():
    try:
        # Note: we might not have the credentials set up properly, so this might fail.
        # But we can check syntax.
        result = supabase.table("visa_cases").select("*", count="exact").range(0, 9).execute()
        print("Success:", result)
    except Exception as e:
        print("Error:", e)

asyncio.run(main())
