## 2025-10-25 - Supabase Pagination Optimization
**Learning:** The Supabase python client evaluates the exact count in `select('*', count='exact')` when returning paginated results while ignoring range and limit. This means pagination data and total counts can be extracted from a single database roundtrip, preventing an unnecessary N+1 query.
**Action:** Always append `count="exact"` to the primary `select` when retrieving paginated query results from Supabase instead of initiating a secondary query just for the count.
