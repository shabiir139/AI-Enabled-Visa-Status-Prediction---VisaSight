## 2024-05-01 - Optimizing Supabase Pagination Counts
**Learning:** Performing a separate `.select("id", count="exact")` query for pagination count creates a redundant database round-trip.
**Action:** Append `count='exact'` to the primary `.select('*')` query. PostgREST efficiently calculates the total based on the applied filters while correctly ignoring the range/limit modifiers for the count calculation, thus doing it all in one round-trip.
