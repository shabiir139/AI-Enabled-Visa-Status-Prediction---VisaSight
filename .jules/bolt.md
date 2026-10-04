## 2024-05-24 - Supabase Pagination Optimization
**Learning:** The codebase was issuing redundant N+1 queries for pagination (one for data, one for the total count). PostgREST calculates the exact total based on applied filters while ignoring range modifiers when `count='exact'` is appended to the primary query.
**Action:** Always combine `.select('*', count='exact')` to halve database load on paginated endpoints.
