## 2025-01-01 - Optimizing Supabase Pagination Queries
**Learning:** When paginating with the Supabase python client, running a separate `select('id', count='exact')` query is an N+1 anti-pattern. PostgREST allows retrieving both the paginated data and the exact total count in a single round trip by passing `count='exact'` to the primary select query.
**Action:** Always append `count='exact'` to the primary `select('*')` query to fetch both data and total rows simultaneously, effectively halving database requests for list endpoints.
