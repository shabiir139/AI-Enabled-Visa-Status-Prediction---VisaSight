## 2024-05-24 - Supabase Pagination N+1 Prevention
**Learning:** Supabase Python client supports getting exact count and paginated rows in a single DB trip via `select('*', count='exact')`. The API was performing two separate queries: one for rows and one for the total count, causing N+1 latency. PostgREST correctly computes total count with applied filters even with `.range()` limits.
**Action:** When implementing pagination, always use the `count='exact'` modifier on the main data fetch query instead of doing a separate count query to halve the number of database round-trips.
