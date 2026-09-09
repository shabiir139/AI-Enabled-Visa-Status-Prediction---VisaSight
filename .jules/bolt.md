## 2024-05-20 - Supabase Pagination Optimization
**Learning:** The Python Supabase client allows fetching both data and total counts in a single network request by passing `count='exact'` to the initial `.select()` query. The count is accessible on the result object even when range limits are applied, bypassing the need for a separate query.
**Action:** Always combine pagination data fetching and count retrieval into a single query in Supabase by using `.select('*', count='exact')` to eliminate redundant database round-trips.
