## 2025-01-26 - Supabase Pagination Double Queries
**Learning:** Found redundant DB queries when fetching paginated lists (data + count). Supabase/PostgREST calculates the total based on applied filters correctly while ignoring range/limit when `count="exact"` is appended to the primary `select("*")`.
**Action:** When implementing pagination with the Supabase Python client, always append `count='exact'` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip.
