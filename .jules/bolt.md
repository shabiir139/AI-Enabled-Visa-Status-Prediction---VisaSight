## 2025-02-14 - Optimize Supabase Count Queries
**Learning:** In Supabase/PostgREST, running a separate `select("id", count="exact")` query for pagination is an unnecessary N+1 pattern that doubles database round-trips. You can append `count="exact"` to the primary `select("*")` data query.
**Action:** Always use `select("*", count="exact")` and extract the count from the response object (`result.count if hasattr(result, 'count') and result.count is not None else len(result.data)`) to optimize pagination performance.
