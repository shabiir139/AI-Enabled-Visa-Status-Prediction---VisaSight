import asyncio
from app.db.supabase import supabase

async def test():
    res = supabase.table("visa_rules").select("*", count="exact").range(0, 1).execute()
    print("Data len:", len(res.data))
    print("Count:", res.count)

if __name__ == "__main__":
    asyncio.run(test())
