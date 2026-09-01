## 2023-10-27 - Optimized Supabase Pagination Count Queries
**Learning:** In Supabase/PostgREST, we can append `count='exact'` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip, avoiding an extra redundant database call.
**Action:** In future implementations of list endpoints, ensure `count='exact'` is merged into the `select` query rather than querying `.select("id", count="exact")` subsequently.
