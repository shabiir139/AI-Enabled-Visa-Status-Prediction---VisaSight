## 2024-10-12 - Supabase Pagination Optimization
**Learning:** In PostgREST/Supabase, retrieving paginated records and the total row count separately causes redundant N+1 queries. PostgREST can calculate the total based on filters while ignoring range/limit modifiers natively if `count='exact'` is passed to the main query.
**Action:** Always append `count='exact'` to the primary `select` query when implementing pagination in Supabase Python client instead of writing a separate `select("id", count="exact")` query.
