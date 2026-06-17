## 2024-06-17 - Supabase N+1 Pagination Optimization
**Learning:** In PostgREST/Supabase, calculating a total count doesn't require a separate database round-trip. By passing `count='exact'` to the primary `select("*")` query, PostgREST calculates the exact total row count matching the filters, while ignoring range/limit modifiers in the query.
**Action:** Always append `count='exact'` to the primary data fetch query for paginated endpoints instead of issuing a secondary `.select("id", count="exact")` query. This halves the database network calls.
