## 2025-03-02 - Single-query pagination & sync route optimization
**Learning:** Using `count="exact"` in `.select()` with `supabase-py` avoids a separate database count query (N+1 query pattern) and retrieves both the data and total exact count in a single database round-trip.
Also, calling `supabase-py` synchronous methods within FastAPI `async def` route handlers can block the main event loop, causing concurrency bottlenecks.
**Action:** Always fetch data and count simultaneously using `.select('*', count="exact")` for paginated endpoints to avoid N+1 queries. When using synchronous clients like `supabase-py`, ensure the FastAPI endpoint uses `def` instead of `async def` so it gets executed in a thread pool and avoids blocking the event loop.
