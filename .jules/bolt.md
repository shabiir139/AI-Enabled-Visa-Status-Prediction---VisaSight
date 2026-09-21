## 2024-09-22 - Optimizing Supabase Pagination Count
**Learning:** For pagination in Supabase Python client, using two queries (one for fetching rows, one for `count="exact"`) results in the N+1 API call pattern.
**Action:** Append `count="exact"` directly to the initial `select("*")` method chain when performing paginated reads, eliminating a redundant query and making it half as expensive for the database connection pool.
