## 2024-08-16 - [Supabase Pagination N+1 Query Optimization]
**Learning:** Found a potential N+1 query problem where `count` in Supabase is executed as a separate request. PostgREST allows appending `count='exact'` to the main `select('*')` query to retrieve data and count simultaneously in a single round-trip.
**Action:** Append `count='exact'` to the initial data fetch and utilize the `.count` attribute on the resulting object to avoid double-querying.
