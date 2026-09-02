## 2025-01-01 - Supabase N+1 Count Pagination
**Learning:** Performing separate count queries for pagination in Supabase is redundant and increases database round-trips.
**Action:** Always append `count='exact'` to the primary select query to fetch data and count simultaneously.
