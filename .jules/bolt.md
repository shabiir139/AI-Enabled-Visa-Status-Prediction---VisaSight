
## 2025-03-23 - [Supabase exact count syntax]
**Learning:** Combining Supabase `.select("*")` queries with a total count via `.select("*", count="exact")` significantly improves latency by halving database roundtrips. When mocking or receiving the execution object from Supabase with this modifier, the `total` parameter is accessed as an attribute on the result object (`result.count`), distinct from `result.data`.
**Action:** When writing pagination queries with the Supabase client, avoid splitting the data query and the count query. Use `select("*", count="exact")` directly on the chain.
