
## 2024-05-18 - [Backend Performance: Supabase N+1 count query]
**Learning:** Using Python Supabase Client, appending `count='exact'` to a `select('*')` query retrieves both paginated records and the total row count in a single database round-trip. This avoids redundant N+1 queries. PostgREST correctly calculates the total based on applied filters while ignoring range/limit modifiers.
**Action:** Consistently combine `select('*', count='exact')` when retrieving paginated lists from Supabase, removing the need to issue an identical filter query just for the count.
