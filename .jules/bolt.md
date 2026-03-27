
## 2025-05-18 - [Offloading Synchronous Operations to Threadpool]
**Learning:** The Supabase Python client executes synchronous blocking I/O calls. Using `async def` for FastAPI endpoints containing these calls blocks the main async event loop, causing severe latency for all concurrent requests.
**Action:** Change `async def` to `def` for endpoints with synchronous CPU-bound operations or blocking I/O (like Supabase DB queries). This offloads the execution to FastAPI's thread pool, allowing the event loop to continue serving other concurrent requests.
