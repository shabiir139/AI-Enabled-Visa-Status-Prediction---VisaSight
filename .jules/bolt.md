## 2025-05-19 - Pagination N+1 Query Fix
**Learning:** Supabase Python client's pagination approach (`select('*')` followed by a separate `select('id', count='exact')`) can be optimized. Adding `count='exact'` to the primary `select` query (`select('*', count='exact')`) retrieves both paginated data and total count in a single database round-trip without affecting the returned data.
**Action:** Always append `count='exact'` directly on the primary query when paginating with Supabase to avoid the N+1 count query.
