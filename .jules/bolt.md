## 2024-08-12 - Supabase Pagination Optimization
**Learning:** Supabase Python client allows retrieving both paginated data and the exact row count in a single query by appending `count="exact"` to the `.select()` modifier.
**Action:** Always append `count="exact"` to the primary query and read `result.count` to avoid redundant N+1 counting queries when implementing pagination with Supabase.
