## 2024-05-14 - Optimize Supabase Count N+1 Query
**Learning:** Found an N+1 query problem in `backend/app/api/cases.py` where a separate count query was being made alongside the data fetch. Supabase supports `count='exact'` in the main `select('*', count='exact')` query, which avoids a redundant database round-trip.
**Action:** When implementing pagination with Supabase, append `count='exact'` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip. This avoids redundant N+1 queries.
