## 2024-05-24 - Supabase Pagination Optimization
**Learning:** When fetching paginated data with Supabase, executing a separate `.select("id", count="exact")` query is an N+1 performance bottleneck. Using `.select("*", count="exact")` on the primary query returns both the records and the total row count (respecting filters while ignoring range limits) in a single round-trip.
**Action:** Always append `count="exact"` to the primary `select` query when implementing pagination with Supabase to halve database queries.
