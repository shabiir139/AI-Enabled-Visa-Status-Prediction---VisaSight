
## 2024-04-02 - Supabase exact count optimization
**Learning:** Supabase Python client can fetch paginated data and the exact total count in a single roundtrip by adding `count="exact"` to the primary `.select()` query (e.g., `.select("*", count="exact")`). This eliminates the need for N+1 queries during pagination when fetching both data and total length.
**Action:** When writing pagination queries, always bundle the `count` attribute in the main `.select()` statement instead of issuing a secondary `.select("id", count="exact")` query. Extract the count via `result.count if hasattr(result, 'count') and result.count is not None else len(result.data)`.
