
## 2025-02-26 - Single Round-Trip Pagination with Supabase
**Learning:** Using `.select("*", count="exact")` retrieves both paginated records and the total row count in a single database round-trip, avoiding redundant N+1 queries for the count.
**Action:** Always append `count="exact"` to the primary select query when implementing pagination with the Supabase client to improve backend response times.
