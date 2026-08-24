## 2024-05-18 - Supabase Pagination Optimization
**Learning:** In the Supabase python client, running a secondary query purely for `count="exact"` leads to an N+1 query problem, increasing latency and potentially missing complex filters applied to the main query.
**Action:** Append `count="exact"` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip. PostgREST handles the count before limit/range modifiers are applied.
