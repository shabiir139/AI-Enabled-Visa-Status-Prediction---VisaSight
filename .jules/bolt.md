## 2025-02-28 - Supabase Exact Count Parsing
**Learning:** When using `count='exact'` in the Supabase Python client, the total count is available on the exact returned response object as `result.count`, separate from `result.data`. If there are no rows or the server doesn't return count, it could be `None`.
**Action:** When extracting the count from a single query via `count='exact'`, always use a fallback pattern like `result.count if hasattr(result, 'count') and result.count is not None else len(result.data)` to prevent crashes and ensure a correct total count.
