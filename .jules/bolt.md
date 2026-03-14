
## 2025-03-14 - Optimize synchronous endpoints by avoiding async def

**Learning:** In FastAPI, if you use `async def` for an endpoint that calls synchronous, blocking code (like the synchronous `supabase` python client or CPU-bound ML predictions via `XGBoost`/`LightGBM`), it blocks the single main event loop, causing severe bottlenecks. Using `def` instead of `async def` makes FastAPI run the endpoint in a separate thread pool automatically, keeping the main loop unblocked.
**Action:** Always check if an endpoint actually `await`s asynchronous calls. If it only executes synchronous DB queries or heavy compute, define it with `def` rather than `async def`.

## 2025-03-14 - Optimize Supabase pagination by combining data and count fetching

**Learning:** When building paginated endpoints, executing a query for the data and a separate query for the total count results in unnecessary N+1 overhead and doubles the network roundtrips to the DB. With `supabase-py`, you can pass `count="exact"` to the `.select("*")` method. This returns both the requested page of data (`result.data`) and the total count matching the query (`result.count`) in a single execution.
**Action:** When implementing pagination with Supabase, merge the count query into the data query using `.select('*', count='exact')` to halve database roundtrips.
