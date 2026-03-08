## 2025-03-08 - Supabase Pagination Optimization
**Learning:** In Supabase, you can fetch both paginated data and the exact row count in a single query by using `.select("*", count="exact")`. The Python client automatically parses this count and attaches it to `result.count`, saving an additional roundtrip compared to a separate `.select("id", count="exact")` query.
**Action:** Always use `.select("...", count="exact")` when building pagination endpoints to prevent N+1 queries.
