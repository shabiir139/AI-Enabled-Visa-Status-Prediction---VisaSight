## 2024-09-19 - Consolidate Supabase Pagination Queries
**Learning:** Found an anti-pattern in the codebase where paginated Supabase endpoints were performing two separate database round-trips: one to fetch the data and a second one to retrieve the total count for pagination.
**Action:** When implementing pagination with the Supabase python client, always append `count='exact'` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip. This avoids N+1 queries.
