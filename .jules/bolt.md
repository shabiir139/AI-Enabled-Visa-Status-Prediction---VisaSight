## 2024-08-25 - Supabase Pagination N+1 Query Optimization
**Learning:** When paginating with Supabase, executing a separate query to get the total count results in unnecessary database round-trips and duplicated filter logic (N+1 query problem). PostgREST supports returning both paginated rows and the total count in a single request.
**Action:** Append `count='exact'` to the initial `select()` query (e.g., `select("*", count="exact")`) and retrieve the total from `result.count`. This cuts database round-trips in half and ensures filter consistency.
