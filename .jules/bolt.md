## 2025-07-25 - Supabase Pagination Optimization
**Learning:** PostgREST (Supabase) supports calculating the total count of rows based on applied filters in a single request by appending `count='exact'` to the `select` query, completely eliminating the need for a second N+1 count query.
**Action:** When implementing pagination with Supabase `select` queries, always use `select('*', count='exact')` instead of making a separate query for the total count.
