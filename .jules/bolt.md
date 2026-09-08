## 2024-05-18 - Supabase Pagination N+1 Query Fix
**Learning:** Supabase Python client (PostgREST) supports retrieving both the paginated records and the total count in a single round-trip by appending `count='exact'` to the primary `.select('*')` query. PostgREST correctly computes the total based on applied filters, ignoring range limits.
**Action:** Always use `.select('*', count='exact')` when performing pagination instead of dispatching a separate count query to avoid redundant network overhead and keep filters perfectly synchronized.
