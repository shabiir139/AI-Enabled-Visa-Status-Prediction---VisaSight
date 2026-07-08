## 2024-05-18 - Supabase Count Query Optimization
**Learning:** Supabase Python client can retrieve the total count alongside paginated records in a single database round-trip by appending `count='exact'` to the primary `select('*')` query. This avoids N+1 queries or redundant full table scans for count.
**Action:** Always include `count='exact'` in the main `select` query when paginating data with the Supabase client, and access it via `result.count`, handling potential None values.
