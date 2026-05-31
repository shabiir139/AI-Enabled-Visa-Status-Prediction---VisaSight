## 2024-05-31 - Supabase N+1 Pagination Optimization
**Learning:** Using separate queries for `.select("*")` and `.select("id", count="exact")` causes an unnecessary DB roundtrip, which is a common N+1 pattern in Supabase.
**Action:** When implementing pagination, always append `count="exact"` to the primary data fetch query and use `result.count` to avoid redundant database calls.
