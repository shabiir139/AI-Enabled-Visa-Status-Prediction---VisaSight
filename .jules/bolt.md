## 2025-02-12 - Optimize Supabase Pagination Queries
**Learning:** Supabase / PostgREST supports retrieving the total row count in the same request as paginated records by adding `count="exact"` to the primary `select()` call, ignoring range/limit modifiers. This avoids an N+1 query and guarantees filters are strictly synchronized.
**Action:** Always append `count="exact"` to the primary select query when implementing pagination in Supabase, eliminating redundant `.execute()` calls.
