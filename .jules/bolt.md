## 2024-05-19 - Fast Pagination with Supabase

**Learning:** When retrieving a paginated list of records with a total count in Supabase, using two separate queries (one for data, one for count) causes a redundant N+1 round-trip performance bottleneck.
**Action:** Append `count='exact'` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip, avoiding redundant N+1 queries.
