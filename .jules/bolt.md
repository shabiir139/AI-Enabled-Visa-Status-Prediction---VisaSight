
## 2024-05-24 - Supabase Pagination Optimization
**Learning:** When paginating with Supabase, executing a separate '.select("id", count="exact")' query causes unnecessary database roundtrips (N+1 query problem for counting). Using '.select("*", count="exact")' fetches both the paginated data and the total row count in a single network request. The 'count' attribute is directly accessible on the returned response object (e.g., 'result.count').
**Action:** Always combine data retrieval and exact counting into a single '.select("*", count="exact")' query when performing pagination with the Supabase Python client.
