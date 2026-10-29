## 2024-05-24 - Supabase Pagination Optimization
**Learning:** The Supabase Python client supports combining `select('*')` with `count='exact'` in a single query, which automatically calculates the total count based on applied filters while ignoring range/limit modifiers.
**Action:** Always append `count='exact'` to the primary `select` query when implementing pagination to avoid redundant count queries and reduce database round-trips by 50%.
