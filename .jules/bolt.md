## 2024-06-28 - Optimize pagination querying by combining exact count

**Learning:** When retrieving paginated records using Supabase/PostgREST, adding `count="exact"` to the primary `select("*")` statement eliminates the need for an N+1 query pattern (where a second separate `select` is fired just for the total count). Supabase calculates the exact total row count matching the applied filters before applying range/limit bounds, attaching it directly to the response metadata (`result.count`).

**Action:** Always bundle `count="exact"` inside the main `select` query when building paginated endpoints, rather than running separate count queries, effectively halving the database overhead.
