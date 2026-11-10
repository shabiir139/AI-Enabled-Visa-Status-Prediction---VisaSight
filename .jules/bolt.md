## 2024-11-10 - Supabase Pagination Optimization
**Learning:** Supabase Python client can execute an extra database query to get the total count for pagination.
**Action:** When querying with `.select("*")` and `.range()`, pass `count="exact"` in `.select("*", count="exact")` to fetch the total count alongside data in one request, bypassing an extra N+1 database round-trip. This takes advantage of PostgREST's design.
