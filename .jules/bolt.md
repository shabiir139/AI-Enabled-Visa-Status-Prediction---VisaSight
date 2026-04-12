
## 2024-05-30 - [Combine Pagination Queries in Supabase]
**Learning:** Supabase supports returning the count natively in paginated API queries using `.select("*", count="exact")` (available via PostgREST). Fetching the count separately results in an N+1 query issue which is costly for latency.
**Action:** Always combine pagination data fetching with total count retrieval by setting `count="exact"` in the `.select()` statement and extracting the count from the single response object via `result.count`.
