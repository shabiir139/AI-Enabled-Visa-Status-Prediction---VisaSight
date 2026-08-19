## 2024-08-19 - Supabase Pagination Optimization
**Learning:** Supabase Python client can retrieve the total row count along with paginated data in a single round-trip by appending `count='exact'` to the main `select('*')` query. This avoids N+1 queries during paginated list endpoints where the count logic repeats the same filtering operations.
**Action:** When implementing pagination with Supabase, append `count='exact'` to the primary `select` query and extract `total = result.count` to eliminate the redundant DB query for calculating total items.
