## 2024-05-24 - Supabase Pagination Optimization
**Learning:** Implementing pagination with a separate count query in Supabase causes N+1 query problems. PostgREST allows retrieving both paginated records and total count in a single database round-trip by appending `count='exact'` to the main `select('*')` query.
**Action:** Always append `count='exact'` to the primary query and read `result.count` to avoid redundant database calls when paginating.
