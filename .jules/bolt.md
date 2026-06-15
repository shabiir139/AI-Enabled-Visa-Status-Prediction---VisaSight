## 2025-02-28 - Optimize Supabase Count Queries
**Learning:** PostgREST automatically filters count calculations even when combined with a data fetch query. When implementing pagination, doing `.select("*", count="exact")` safely retrieves both data points in a single database roundtrip without returning an incorrect total count due to `.range()` limiting.
**Action:** Use `select("*", count="exact")` with `result.count` and fallback `len(result.data)` rather than executing a separate `count="exact"` query when paginating data using the Supabase client.
