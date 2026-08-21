## 2024-05-18 - Supabase Single-Query Pagination
**Learning:** Supabase Python client can retrieve the total row count along with paginated records in a single database round-trip by appending `count='exact'` to the primary `select('*')` query. This avoids redundant N+1 queries. PostgREST calculates the total based on filters while ignoring range limits.
**Action:** Always use `select('*', count='exact')` when implementing pagination with Supabase to halve database round-trips.
