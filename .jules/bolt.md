## 2024-09-04 - Supabase Count Query N+1 Optimization
**Learning:** Supabase Python client allows combining paginated select queries with exact counts in a single query (`select("*", count="exact")`), avoiding a redundant N+1 query pattern where the count is queried separately from the data.
**Action:** Always use `select("*", count="exact")` and extract the count from `result.count` (with `hasattr` safety check) when building paginated endpoints to save database round-trips.
