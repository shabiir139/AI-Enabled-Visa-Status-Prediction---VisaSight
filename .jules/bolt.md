# Bolt's Journal

## 2026-02-20 - Backend Pagination Optimization
**Learning:** Supabase Python client supports `select(..., count='exact')` which fetches both data and total count in a single request. This is a critical pattern to avoid N+1 queries in paginated endpoints.
**Action:** Always check for `count="exact"` usage when implementing or optimizing pagination in Supabase-backed services.
