## 2024-07-03 - Supabase Pagination Redundant Query
**Learning:** Combining Supabase `select("*")` with `count="exact"` returns both data and the total count correctly based on filters but ignores range, avoiding N+1 DB round-trips for pagination.
**Action:** Always append `count="exact"` to the primary query during pagination with Supabase to avoid firing a separate count query.
