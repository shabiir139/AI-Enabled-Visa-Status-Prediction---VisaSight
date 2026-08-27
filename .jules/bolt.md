## 2024-05-24 - [Supabase N+1 Pagination Optimization]
**Learning:** Found a classic N+1 querying issue in backend pagination. Supabase can fetch paginated results AND total exact row counts in a single query by using `select('*', count='exact')`.
**Action:** Replace two distinct DB queries (one for data, one for count) with a single `select` query to avoid the extra round trip. This cuts database latency in half for pagination endpoints.
