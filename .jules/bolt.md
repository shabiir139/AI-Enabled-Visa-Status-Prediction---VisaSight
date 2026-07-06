## 2024-07-06 - Supabase Pagination Optimization
**Learning:** When retrieving paginated records using the Supabase client, performing a separate `.select('id', count='exact')` query after the main query causes an unnecessary N+1 round-trip to the database, and introduces the risk of omitting query filters on the count query.
**Action:** Use `.select('*', count='exact')` on the primary query to retrieve both the records and the total count in a single database round-trip. Extract the count via `result.count if hasattr(result, 'count') and result.count is not None else len(result.data)`.
