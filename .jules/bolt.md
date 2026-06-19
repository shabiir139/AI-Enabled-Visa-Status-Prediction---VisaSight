
## 2025-05-18 - Supabase Single-Query Pagination Optimization
**Learning:** In Supabase/PostgREST, combining `select("*", count="exact")` accurately calculates the total row count (respecting active filters like `.eq()`) while completely ignoring the limits applied by `.range()`. This allows fetching a single page of data and the total possible row count in one database round-trip.
**Action:** Always append `count='exact'` to the primary query and parse `result.count` to avoid redundant N+1 aggregate count queries when implementing pagination with the Supabase client.
