## 2024-09-18 - Supabase Pagination Optimization
**Learning:** The Supabase PostgREST client can retrieve both paginated rows and the total unpaginated row count in a single database round-trip by passing `count='exact'` to the initial `select()` query. This avoids a common N+1 anti-pattern where a secondary count query is issued, halving database latency for paginated endpoints.
**Action:** Always append `count='exact'` to the primary `select()` when pagination is required instead of running a redundant secondary count query.
