## 2024-05-15 - [Initial Setup]
**Learning:** [Setting up bolt journal]
**Action:** [Use for learnings]
## 2024-05-15 - [Backend Pagination Query Optimization]
**Learning:** The synchronous `supabase` python client can block the main FastAPI loop if used in `async def` endpoints, particularly when performing multiple consecutive calls (e.g. one for data, one for count).
**Action:** Always combine pagination data and count into a single query using `.select('*', count='exact')`. For endpoints making synchronous Supabase calls, use `def` instead of `async def` so FastAPI runs them in a thread pool.
