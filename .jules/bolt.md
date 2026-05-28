## 2026-05-28 - Supabase Pagination Exact Count
**Learning:** Implementing pagination with the Supabase client traditionally causes an N+1 query issue. Appending count='exact' to the primary select('*') query retrieves both paginated records and the total row count in a single database round-trip.
**Action:** Always append count='exact' to Supabase pagination queries instead of running a separate count query.
