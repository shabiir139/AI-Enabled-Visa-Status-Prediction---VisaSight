## 2025-02-27 - Supabase Pagination Optimization
**Learning:** Implementing pagination with a separate count query causes a redundant database round-trip (N+1 query problem). Appending count='exact' to the primary select query retrieves both the paginated data and the total row count simultaneously, halving database latency for list endpoints.
**Action:** Always use .select('*', count='exact') for Supabase queries that require both paginated data and a total row count.
