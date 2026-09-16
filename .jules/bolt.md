## 2025-01-30 - Combine Supabase Count Queries
**Learning:** Using the Supabase Python client's `select('*', count='exact')` correctly retrieves the data and the total item count (ignoring pagination limits) in a single API request/database round-trip, avoiding the N+1 API call pattern when performing pagination.
**Action:** When writing Supabase paginated queries, always combine the count modifier with the primary select query instead of executing a second standalone count query.
