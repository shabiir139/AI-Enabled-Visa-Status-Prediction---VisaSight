## 2024-05-18 - Supabase exact count optimization
**Learning:** Supabase Python client supports appending `count="exact"` to paginated `select` queries to retrieve both the data and total count in a single database round-trip, avoiding redundant queries. PostgREST handles calculating the total based on filters, ignoring the limit/range modifiers.
**Action:** Always append `count="exact"` to paginated `select` queries instead of running a separate `select("id", count="exact")` query.
