## 2024-05-18 - Supabase Pagination Optimization
**Learning:** In Supabase/PostgREST, we don't need to perform separate queries to fetch a paginated page of results and to calculate the total row count. `select('*', count='exact')` automatically computes the full table count based on the applied filters, ignoring any `limit` or `range` constraints applied to the data payload.
**Action:** Use `select('*', count='exact')` to eliminate redundant N+1 counting requests, and extract the count safely using `result.count if hasattr(result, 'count') and result.count is not None else len(result.data)`.
