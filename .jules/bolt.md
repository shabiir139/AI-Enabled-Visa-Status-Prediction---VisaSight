## 2025-06-25 - Combine Supabase pagination queries
**Learning:** When implementing pagination with the Supabase client, you can append `count='exact'` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip. This avoids redundant N+1 queries and prevents bugs where filters are accidentally omitted from a separate count query.
**Action:** Always combine the data fetch and total row count query when implementing pagination with Supabase.
