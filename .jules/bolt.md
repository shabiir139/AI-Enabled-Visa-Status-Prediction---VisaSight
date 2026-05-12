## 2025-05-12 - [Supabase N+1 Pagination Optimization]
**Learning:** Performing paginated queries with Supabase clients natively using `.select("*")` followed by a second `.select("id", count="exact")` incurs an unnecessary N+1 round-trip performance penalty to the database.
**Action:** When implementing pagination with the Supabase client, always append `count='exact'` to the primary `.select("*")` query to retrieve both paginated records and the total row count in a single database round-trip. Handle count retrieval natively via `result.count` with a fallback format to prevent crashes.
