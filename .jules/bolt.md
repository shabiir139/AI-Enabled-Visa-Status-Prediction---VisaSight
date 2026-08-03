## 2024-05-18 - Supabase Pagination Optimization
**Learning:** In Supabase, you can retrieve both paginated records and the total row count in a single database round-trip by appending `count='exact'` to the primary `select('*')` query. PostgREST calculates the total based on applied filters while ignoring range/limit modifiers.
**Action:** Always use `select('*', count='exact')` for paginated queries instead of issuing a separate `select('id', count='exact')` query to reduce database roundtrips.
