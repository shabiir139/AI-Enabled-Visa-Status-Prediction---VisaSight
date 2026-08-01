## 2024-08-01 - Optimizing Supabase Pagination Total Count
**Learning:** In Supabase/PostgREST, you can retrieve the total count and the paginated records in a single round-trip by passing `count="exact"` directly to the initial `select()` query. A separate `.select("id", count="exact")` query is a redundant N+1 query and unnecessarily degrades backend API performance.
**Action:** When implementing pagination with the Supabase client, always append `count="exact"` to the primary `select` query and access `result.count`, instead of executing a second standalone count query.
