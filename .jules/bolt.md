## 2024-11-11 - Optimized Supabase Pagination Queries
**Learning:** PostgREST can return the exact row count for a query in a single database round-trip by appending `count='exact'` to the primary `select` query (e.g., `supabase.table('table').select('*', count='exact')`).
**Action:** Always append `count='exact'` to the primary `select` query when both data and total count are required for pagination, to avoid redundant database calls.
