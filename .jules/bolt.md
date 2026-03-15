
## 2025-02-13 - Combine Supabase data fetch and exact count into single query
**Learning:** In Supabase's Python client, fetching a paginated list of records and the total exact count doesn't require two separate `.execute()` calls (one for data, one for count). Passing `count="exact"` into the initial `.select()` method returns both the data array and a `.count` property on the response object.
**Action:** Always use `.select("*", count="exact")` for paginated list endpoints to avoid unnecessary N+1 network round trips to the database, effectively cutting database query latency in half for these routes.
