
## 2025-02-27 - Supabase Client Backend Pagination Optimization
**Learning:** The synchronous Python Supabase client can perform a query to fetch both data and exact row count simultaneously using `.select("*", count="exact")`. The total count is accessible via the `count` attribute of the returned result object (`result.count`).
**Action:** Always use `.select("*", count="exact")` and extract the count from the response object instead of running a redundant duplicate query purely to count rows. This halves the database roundtrips for list endpoints, reducing latency and mitigating N+1-like inefficiencies.
