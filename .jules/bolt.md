## 2024-06-30 - Supabase Single-Roundtrip Pagination
**Learning:** Supabase / PostgREST correctly computes the exact total row count in a single `select("*", count="exact")` query, even when `.range()` or `.limit()` are applied, taking any `.eq()` or `.ilike()` filters into account without needing a secondary database query.
**Action:** Always bundle `count="exact"` in the primary pagination query instead of executing N+1 count-only queries.
