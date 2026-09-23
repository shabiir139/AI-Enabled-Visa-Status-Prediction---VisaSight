## 2024-05-24 - [N+1 query problem in supabase Python client pagination]
**Learning:** Using two separate queries for paginated records and total row count is redundant and error-prone. Supabase PostgREST correctly calculates the total based on applied filters while ignoring range/limit modifiers when `count='exact'` is appended to the primary query.
**Action:** Append `count='exact'` to the primary `select('*')` query when implementing pagination with the Supabase client in Python to save a round-trip and reduce latency.
