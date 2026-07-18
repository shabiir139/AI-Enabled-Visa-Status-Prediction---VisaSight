## 2026-07-18 - Supabase Pagination Redundant Queries
**Learning:** When using the Supabase client for paginated queries, performing a separate `.select("id", count="exact")` query creates a redundant database roundtrip (N+1 query pattern). PostgREST can calculate the total based on filters and ignore range limits in a single request.
**Action:** Append `count='exact'` directly to the primary `.select('*')` query to retrieve both data and the total row count simultaneously, reducing latency and backend load.
