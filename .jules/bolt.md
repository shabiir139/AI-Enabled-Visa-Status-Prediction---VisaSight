## 2024-06-25 - Supabase synchronous execution blocking asyncio
**Learning:** The FastAPI endpoints use `async def` but use the synchronous `supabase-py` client inside them. Because `supabase-py` runs synchronously and does not use `await`, it blocks the main event loop, causing severe latency degradation when serving multiple requests concurrently.
**Action:** Replace `async def` with `def` for FastAPI routes that perform blocking synchronous I/O, allowing FastAPI to execute these in an external thread pool.
