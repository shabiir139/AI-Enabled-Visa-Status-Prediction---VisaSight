## 2024-09-12 - Combine Supabase Queries for Pagination
**Learning:** Supabase / PostgREST correctly calculates the total row count based on applied filters while ignoring range/limit modifiers when `count="exact"` is appended to the primary query. Using two queries (one for data and one for count) is a common but unnecessary bottleneck.
**Action:** Always append `count="exact"` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip, avoiding redundant N+1 queries.
