## 2025-03-07 - [Supabase Pagination Optimization]
**Learning:** [When making paginated queries with the synchronous Supabase python client in FastAPI, avoid executing separate queries for total count and data retrieval. This creates an N+1 query pattern and blocks the main thread twice.]
**Action:** [Use `.select('*', count='exact')` to retrieve both the paginated data and the exact total count in a single database request. Access `result.count` and assign to thread-pooled `def` endpoints to prevent blocking.]
