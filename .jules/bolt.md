## 2026-06-11 - Supabase Pagination Optimization
**Learning:** Implementing pagination with a separate count query in Supabase causes a redundant N+1 query and risks omitting filters. PostgREST allows appending count='exact' to the primary select query to retrieve both paginated records and the total row count in a single database round-trip.
**Action:** Always append count='exact' to the primary select query for pagination and extract the count using fallback logic.
