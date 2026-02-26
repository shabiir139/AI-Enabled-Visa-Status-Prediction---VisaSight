## 2025-05-26 - Async/Sync Mismatch in FastAPI & Supabase
**Learning:** The codebase heavily uses `async def` for FastAPI routes while using the synchronous `supabase` Python client. This blocks the main event loop during database operations, serializing requests. Using `def` for synchronous I/O operations allows FastAPI to offload them to a thread pool, enabling concurrency.
**Action:** When working with synchronous clients (like standard `supabase-py` or `requests`), always use `def` for route handlers, not `async def`.

## 2025-05-26 - Supabase Pagination Optimization
**Learning:** Supabase (PostgREST) supports fetching data and total count in a single query using `.select('*', count='exact')`. The codebase previously used two separate queries (one for data, one for count), doubling the latency.
**Action:** Always use `count='exact'` in the initial select when implementing pagination to reduce round trips.
