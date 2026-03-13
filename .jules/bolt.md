## 2024-03-14 - Blocking the Event Loop with Synchronous Code

**Learning:** Using `async def` for FastAPI endpoints that call synchronous Python operations (like the synchronous Supabase client or CPU-bound ML inference) blocks the main event loop, causing severe latency under concurrent load.
**Action:** Always use `def` for FastAPI endpoints that execute blocking, synchronous code. FastAPI will automatically run these `def` endpoints in an external threadpool, preserving the responsiveness of the main event loop.

## 2024-03-14 - N+1 Query Optimization in Supabase Pagination

**Learning:** Running separate `.select("*")` and `.select("id", count="exact")` queries in Supabase for pagination is redundant and doubles database latency per request.
**Action:** Use `.select("*", count="exact")` in a single query to retrieve both the paginated data and the total record count in one network trip, significantly optimizing list endpoint performance.
