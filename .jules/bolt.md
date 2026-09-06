## 2024-05-24 - Optimize Supabase Pagination
**Learning:** Performing a separate query for the total count of a paginated query in Supabase adds redundant latency, mimicking an N+1 issue.
**Action:** Always append `count="exact"` to the primary `select("*")` query. PostgREST calculates the count based on filters before applying range/limit modifiers.
