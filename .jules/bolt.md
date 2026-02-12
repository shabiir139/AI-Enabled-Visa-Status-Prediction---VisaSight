## 2026-02-12 - Backend Pagination Optimization
**Learning:** The previous implementation of pagination in `visa_cases` and `visa_rules` endpoints used two separate queries: one for data fetching and another for count. This doubled the database round-trips. Supabase/PostgREST supports fetching both in a single query using `.select('*', count='exact')`.
**Action:** Always check for opportunities to combine data fetching and count queries when implementing pagination with Supabase.
