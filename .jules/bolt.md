## 2025-01-01 - Combine Supabase pagination queries for exact count
**Learning:** Supabase Python client allows retrieving the total count and the paginated results in a single round-trip by passing `count='exact'` to the primary `select('*')` query. PostgREST handles the calculation correctly based on filters while ignoring pagination modifiers (range/limit).
**Action:** Always use `select('*', count='exact')` when implementing pagination in Supabase instead of executing a separate count query to avoid redundant database round-trips and potential filter mismatches.
