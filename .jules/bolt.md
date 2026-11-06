## 2024-11-06 - Supabase Pagination Optimization
**Learning:** Supabase PostgREST allows fetching exact row count and paginated data in a single round-trip by appending `count='exact'` to the primary `select` query (e.g., `supabase.table('table').select('*', count='exact')`), avoiding an N+1/redundant query for total count.
**Action:** Always append `count='exact'` to the main `select` when paginating Supabase queries instead of issuing a separate count query.
