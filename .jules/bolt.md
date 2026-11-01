## 2024-05-24 - Supabase Pagination Optimization
**Learning:** Supabase PostgREST correctly calculates the total count based on applied filters while ignoring range/limit modifiers when count='exact' is passed to the primary select query. We were previously making two separate database round-trips for pagination (one for data, one for count) which is inefficient and prone to filter-mismatch bugs.
**Action:** Always append count='exact' to the primary select('*') query to retrieve both paginated records and the total row count in a single database round-trip, avoiding redundant queries.
