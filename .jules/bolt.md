## 2025-02-04 - Supabase Single Query Pagination
**Learning:** The Supabase client supports appending count="exact" to a select("*") query to retrieve both paginated records and the total row count in a single database round-trip. This avoids redundant N+1 queries and prevents bugs where filters are accidentally omitted from a separate count query.
**Action:** Always append count="exact" when performing pagination in Supabase Python client to avoid redundant counting queries.
