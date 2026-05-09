
## 2024-05-09 - Combine Pagination Data and Exact Count with Supabase
**Learning:** In applications using Supabase, executing two separate queries to get paginated data (`select("*")`) and the total row count (`select("id", count="exact")`) introduces a redundant N+1 query problem, increasing network overhead and latency.
**Action:** Append `count="exact"` to the primary data fetch query (e.g., `.select("*", count="exact")`) to return both the data and the total exact row count in a single database round-trip. Robustly parse the exact count using `total = result.count if hasattr(result, 'count') and result.count is not None else len(result.data)`.
