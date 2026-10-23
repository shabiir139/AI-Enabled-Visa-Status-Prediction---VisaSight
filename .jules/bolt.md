## 2025-10-23 - Supabase Pagination Optimization
**Learning:** In the Supabase python client, implementing pagination using a separate count query (e.g. `select('id', count='exact')`) causes a redundant N+1 database roundtrip.
**Action:** Always append `count='exact'` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip. PostgREST correctly calculates the total based on applied filters while ignoring range/limit modifiers.
