## 2026-07-07 - Pagination Optimization
**Learning:** Supabase Python client can fetch paginated data and the exact row count in a single database round-trip by appending count='exact' to the primary select query. This prevents N+1 query problems where a separate count query is accidentally omitting filters or causing redundant database load.
**Action:** Always append count='exact' to the primary query and access the count via result.count instead of executing a separate query.
