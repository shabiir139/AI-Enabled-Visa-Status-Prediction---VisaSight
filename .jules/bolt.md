
## 2025-02-28 - [Batch pagination database queries]
**Learning:** In Supabase Python client querying, calling `.select('*', count='exact')` is a powerful optimization that returns both the data and the total record count in a single query result. The `count` is then available as `result.count` and avoids an N+1 database request for the pagination count.
**Action:** Always prefer `.select('*', count='exact')` combined with direct extraction from the response over querying data first and then doing a second `.select('id', count='exact')` query.
