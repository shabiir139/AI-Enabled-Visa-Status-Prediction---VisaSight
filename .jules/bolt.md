## 2024-10-30 - Supabase Single Round-Trip Pagination
**Learning:** Supabase Python client can fetch both paginated data and the total exact count in a single database round-trip by appending `count='exact'` to the initial `select('*')` query. This eliminates redundant N+1 queries. PostgREST calculates the total based on applied filters while ignoring range/limit modifiers.
**Action:** Always use `select('*', count='exact')` when implementing pagination, and access the total via `result.count if hasattr(result, 'count') and result.count is not None else len(result.data)`.
