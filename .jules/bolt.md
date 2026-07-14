## 2026-03-10 - Supabase Pagination Optimization
**Learning:** Supabase PostgREST allows retrieving both the data and the exact row count in a single query by appending `count="exact"` to the select method (e.g., `select("*", count="exact")`). It automatically factors in any filters applied to the query while ignoring pagination limits, saving a redundant N+1 query.
**Action:** When implementing pagination with Supabase in Python, always append `count="exact"` to the main query and extract the count from the single result object to eliminate an unnecessary database round-trip.
