## 2025-02-18 - Optimized Supabase Pagination Queries
**Learning:** Supabase (PostgREST) Python client supports fetching `count="exact"` in the `.select()` method, eliminating the need for a separate query to get the total count for pagination.
**Action:** When implementing pagination with Supabase, always use `.select("*", count="exact")` instead of a separate count query to halve the number of database round-trips.
