## 2025-08-05 - Supabase Pagination Optimization
**Learning:** Supabase Python client can retrieve both paginated data and the exact total count in a single query by using `select("*", count="exact")`, which saves an entire database round-trip. PostgREST handles the total computation with the filters natively without being constrained by range limits.
**Action:** Always append `count="exact"` to the primary query and fetch the result using `result.count` to avoid redundant N+1 query patterns for pagination.
