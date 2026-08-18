## 2026-08-18 - Supabase Pagination Count Optimization
**Learning:** Supabase python client doesn't need separate queries for count and data when paginating. The `count="exact"` parameter inside the initial `select` handles the total count computation dynamically on the backend while correctly adhering to PostgREST filters and ignoring limits/ranges.
**Action:** Always append `count='exact'` to paginated `select('*')` calls to prevent N+1 queries.
