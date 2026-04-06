# Bolt's Journal

## 2025-02-23 - Optimize Pagination Queries in Database Client
**Learning:** In Supabase, pagination queries that require returning both the data and the total item count often default to doing two separate sequential queries (one for `.select('*')` and one for `.select('id', count='exact')`). This results in unnecessary double network roundtrips and 2x database processing time.
**Action:** Always combine them into a single request by utilizing the `.select('*', count='exact')` argument. The count will be accessible directly on the result object (`result.count`). Remember to add a fallback parser (`len(result.data)`) in case the count attribute is missing on error or empty results.