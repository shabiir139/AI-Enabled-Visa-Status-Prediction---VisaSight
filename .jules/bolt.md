## 2024-05-18 - Supabase Single-Query Pagination
**Learning:** Supabase Python client can retrieve both paginated records and the total row count in a single database round-trip by appending count="exact" to the primary select query.
**Action:** Always append count="exact" to the primary query for paginated endpoints to avoid N+1 query problems and ensure filters are applied consistently.
