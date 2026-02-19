## 2024-05-23 - [Supabase Query Optimization]
**Learning:** Supabase Python client's `select(..., count="exact")` returns the total count in `result.count`, allowing for efficient single-query pagination.
**Action:** Always use `count="exact"` in the initial query when pagination metadata is needed, instead of a separate count query.
