## 2024-06-29 - Supabase Pagination Optimization
**Learning:** Using `select('*', count='exact')` in Supabase retrieves both the paginated records and the total row count in a single database round-trip, avoiding redundant N+1 queries. PostgREST correctly calculates the total based on applied filters while ignoring range/limit modifiers.
**Action:** When implementing pagination with the Supabase client, always append `count='exact'` to the primary `select` query instead of making a separate count query.
