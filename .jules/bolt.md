## 2024-05-15 - [Supabase N+1 Pagination Optimization]
**Learning:** Found N+1 query problem with pagination in Supabase calls. Instead of running a primary `select` query and then a separate `select(..., count="exact")` query, which takes two round-trips to the database, Supabase Python Client allows adding `count="exact"` directly to the initial query. This returns both the data and the total count in one go.
**Action:** Consolidate multiple queries into a single query with count when doing pagination.
