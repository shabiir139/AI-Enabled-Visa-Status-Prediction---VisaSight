## 2025-07-16 - Supabase Pagination Optimization
**Learning:** Supabase Python client's `select('*')` method accepts `count='exact'`. This allows retrieving both the paginated records and the total row count in a single database round-trip. PostgREST calculates the total based on applied filters while ignoring range limits.
**Action:** Always append `count='exact'` to primary paginated Supabase queries and extract the total from `result.count` instead of performing redundant separate queries.
