## 2024-04-22 - [Combined Supabase Pagination]
**Learning:** Supabase query endpoints can optimize pagination overhead by eliminating the N+1 query problem commonly used to fetch a data set and a count separately. Using `.select("*", count="exact")` merges these operations into a single query block, with the data returned in `result.data` and the exact integer stored in `result.count`.
**Action:** Use `.select("*", count="exact")` instead of separate `select("*")` and `.select("id", count="exact")` statements when refactoring endpoints requiring paginated totals to reduce network overhead.
