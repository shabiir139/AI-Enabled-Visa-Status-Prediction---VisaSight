## 2024-06-09 - Supabase Pagination Optimization
**Learning:** Supabase (PostgREST) can return both paginated records and the total row count in a single query by appending `count='exact'` to the primary `select('*')`. It correctly calculates the total based on filters while ignoring range/limit modifiers.
**Action:** Always combine data fetching and counting into a single query when paginating with Supabase to avoid redundant database round-trips.
