
## 2024-05-18 - [PostgREST Pagination Optimization]
**Learning:** In Supabase/PostgREST, we can request `count="exact"` in the primary `.select()` query to fetch both the paginated data and the total row count in a single database round-trip. This prevents needing a separate `.execute()` query purely for calculating the total count, halving database latency for paginated endpoints.
**Action:** When implementing pagination on Supabase data, always use `select("*", count="exact")` and extract the count directly from the response object via `result.count` instead of performing a secondary query.
