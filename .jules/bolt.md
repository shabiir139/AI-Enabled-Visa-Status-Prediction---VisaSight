## 2024-03-18 - Supabase Pagination and Count Optimization
**Learning:** Found N+1 query pattern where separate database calls are made for paginated records and exact count in Supabase. Supabase/PostgREST correctly evaluates count based on filters while ignoring range limits.
**Action:** When using Supabase python client for pagination, combine `select('*', count='exact')` to retrieve data and total row count in a single round-trip instead of making redundant queries. Ensure `count` property is properly handled in the response.
