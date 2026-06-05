## 2026-06-05 - Supabase Pagination Optimization
**Learning:** When implementing pagination with the Supabase client, appending `count='exact'` to the primary `select('*')` query retrieves both paginated records and the total row count in a single database round-trip, avoiding redundant N+1 queries. PostgREST correctly calculates this based on filters while ignoring range/limit modifiers.
**Action:** Always use the `count='exact'` parameter in the primary query for paginated Supabase endpoints to minimize database round-trips.
