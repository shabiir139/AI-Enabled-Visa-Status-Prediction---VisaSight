## 2025-02-28 - Optimize Supabase pagination queries
**Learning:** When using the Supabase client for pagination, making separate queries for the data and the count causes an N+1 query problem. PostgREST allows appending `count='exact'` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip.
**Action:** Always append `count='exact'` to the primary `select('*')` query when paginated records and total count are both needed.
