## 2024-05-22 - [Supabase N+1 Pagination Optimization]
**Learning:** [When implementing pagination with the Supabase Python client, using a separate `select("id", count="exact")` query creates an N+1 performance bottleneck. Appending `count="exact"` directly to the primary `select("*")` query allows fetching both the paginated data and the total row count in a single database round-trip.]
**Action:** [Always use `select("*", count="exact")` when pagination is needed to avoid redundant count queries and extract the count directly from `result.count`.]
