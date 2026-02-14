## 2026-02-14 - [Supabase Query Optimization]
**Learning:** Supabase Python client supports `.select("*", count="exact")` to fetch data and total count in a single request.
**Action:** Replace separate data and count queries with a single query using `count="exact"` in paginated endpoints.
