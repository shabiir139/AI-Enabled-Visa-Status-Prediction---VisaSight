## 2024-11-20 - [Supabase N+1 Pagination Queries]
**Learning:** The Supabase client for Python allows fetching both paginated records and the total count in a single query by using `select('*', count='exact')`. This avoids redundant N+1 queries.
**Action:** When implementing pagination with the Supabase client, combine data retrieval and total counting into a single database round-trip by appending `count='exact'` to the initial query.
