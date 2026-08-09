## 2025-02-14 - Optimize Supabase Count Queries
**Learning:** Performing a separate select query with count='exact' to get the total rows for pagination introduces an unnecessary database roundtrip (N+1 issue), as PostgREST can calculate the count on the primary query based on the applied filters while ignoring range limits.
**Action:** Always append count='exact' to the primary select query to fetch both the paginated records and the total row count simultaneously.
