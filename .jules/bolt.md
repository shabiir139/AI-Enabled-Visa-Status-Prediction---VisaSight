## 2025-07-05 - Optimize Supabase Pagination Count
**Learning:** PostgREST allows calculating exact total count alongside the paginated data query by appending `count='exact'` to the `select()` call, which avoids duplicate filter logic and a redundant N+1 query.
**Action:** Always combine the data query and the count query into a single Supabase request by using `select('*', count='exact')` when retrieving paginated records.
