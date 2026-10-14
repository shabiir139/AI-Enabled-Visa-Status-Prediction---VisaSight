## 2024-10-24 - Supabase N+1 Pagination Optimization
**Learning:** Using Supabase PostgREST client in python, querying pagination records with a separate total count `.select("id", count="exact")` query is an N+1 pattern that causes unnecessary extra database roundtrips and connection latency.
**Action:** Always combine the total count calculation with the primary paginated query by appending `count="exact"` to the `.select("*", count="exact")` modifier. The result object will contain both the data and `.count`.
