## 2024-08-10 - Supabase Single-Query Pagination Optimization
**Learning:** Supabase Python client allows fetching paginated data and the exact total count in a single round-trip by appending `count='exact'` to the initial `select('*')` query. This completely eliminates the N+1 query problem and ensures filters are consistent without requiring a separate, redundant count query.
**Action:** Always append `count='exact'` to paginated Supabase `.select()` queries and retrieve the total via `result.count` instead of executing a second standalone count query.
