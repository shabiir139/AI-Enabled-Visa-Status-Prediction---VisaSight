## 2025-02-18 - Supabase Pagination Optimization
**Learning:** Backend pagination queries should use `.select('*', count='exact')` to retrieve data and the total count in a single request, avoiding separate count queries (N+1 anti-pattern).
**Action:** When implementing paginated lists with Supabase, append `count='exact'` to the main query's select statement and parse the count using `result.count if hasattr(result, 'count') and result.count is not None else len(result.data)`.
