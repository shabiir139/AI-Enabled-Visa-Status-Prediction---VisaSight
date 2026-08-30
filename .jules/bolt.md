## 2024-06-25 - Exact Count
**Learning:** Using count="exact" with Supabase PostgREST client requires checking if `result.count` exists. PostgREST handles the count while ignoring range limits.
**Action:** Always check `result.count` and fallback to `len(result.data)` if none.
