## 2024-07-28 - Optimize Supabase Count Queries
**Learning:** Supabase Python client can retrieve the total count of rows for paginated queries without a separate query. By passing `count='exact'` to the initial `select()` statement, PostgREST calculates the total based on applied filters while ignoring range limits, returning it in `result.count`.
**Action:** Always combine paginated data retrieval and exact counts into a single `.select('*', count='exact')` query in Supabase to eliminate redundant N+1 queries. Ensure to handle `result.count is not None`.
