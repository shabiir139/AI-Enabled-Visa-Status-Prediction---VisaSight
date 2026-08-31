## 2024-05-24 - [Supabase Pagination Round-Trip Reduction]
**Learning:** Using Supabase PostgREST for pagination traditionally leads to redundant query round-trips for the exact count, however `select('*', count='exact')` automatically returns both paginated results and the exact count for all filters in a single request.
**Action:** Always append `count='exact'` to Supabase pagination queries rather than explicitly creating a duplicate `select('id', count='exact')` query.
