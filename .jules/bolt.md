## 2024-05-24 - [Supabase N+1 Pagination Elimination]
**Learning:** Using `count='exact'` directly within a Supabase `.select("*")` query completely eliminates the need for a secondary count query, effectively halving database latency for paginated endpoints.
**Action:** Always fetch data and exact count simultaneously when paginating in Supabase using the PostgREST feature, safely parsing the response using `result.count if hasattr(result, 'count') and result.count is not None else len(result.data)`.
