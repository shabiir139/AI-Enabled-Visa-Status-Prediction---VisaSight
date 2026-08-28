## 2024-05-18 - Supabase Pagination Exact Count Optimization
**Learning:** For Supabase pagination in Python, calling `count='exact'` in a separate query repeats network roundtrips and filter overhead, leading to N+1-like performance. Appending `count='exact'` to the main `select('*')` retrieves data and the total row count simultaneously (PostgREST ignores limit/range for the total count).
**Action:** Always append `count='exact'` to the primary `select('*')` query when paginating data to consolidate database hits, and retrieve the count via `result.count`.
