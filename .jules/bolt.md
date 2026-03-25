
## 2024-05-28 - [Combine Supabase Python Client Pagination Counts]
**Learning:** The Supabase Python client can retrieve the exact count of rows alongside the queried data in a single request using `.select("*", count="exact")`. The total is available as `result.count`, preventing the common N+1 query pattern where a separate query is executed solely for pagination counting.
**Action:** When building pagination endpoints interacting with Supabase, include `count="exact"` in the primary `select` call and read from `result.count` to halve the number of DB roundtrips.
