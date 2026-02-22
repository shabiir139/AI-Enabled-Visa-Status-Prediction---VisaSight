## 2026-02-22 - [Supabase Count Optimization]
**Learning:** The Supabase Python client supports `select('*', count='exact')` to retrieve the total count alongside the data in a single request. The codebase frequently employs a pattern of two separate queries (one for data, one for count), which doubles the network round trips and DB load.
**Action:** When implementing pagination with Supabase, consolidate data retrieval and total count into a single query using `count='exact'` to improve performance.
