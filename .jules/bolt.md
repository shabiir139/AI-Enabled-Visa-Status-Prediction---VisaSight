## 2025-05-23 - [Supabase Count Optimization]
**Learning:** Supabase Python client supports `.select('*', count='exact')` which returns the count in the result object (`result.count`). Using a separate query for count is an anti-pattern that doubles latency.
**Action:** Always use `count='exact'` in the main query when pagination is needed, instead of a separate count query.
