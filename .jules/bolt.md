## 2024-05-24 - Supabase Python Client Pagination Optimization
**Learning:** The Supabase Python client executes two separate network requests if you perform a paginated `.select()` and then a separate `.select('id', count='exact')` for the total count.
**Action:** When performing pagination with the Supabase Python client, always pass `count='exact'` to the initial data query (e.g., `supabase.table(...).select('*', count='exact')`). The total count will be available as `result.count`, saving a full database roundtrip and halving the network overhead for paginated endpoints.
