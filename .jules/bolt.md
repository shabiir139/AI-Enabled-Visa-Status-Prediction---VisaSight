## 2025-02-12 - Supabase Pagination Optimization
**Learning:** When using the Supabase client for paginated queries, executing a separate query just to get the total count creates an N+1 query bottleneck.
**Action:** Always append `count='exact'` to the primary query string or `select()` call to fetch both data and the total row count in a single database round-trip. PostgREST handles the calculation optimally based on the applied filters.
