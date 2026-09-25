## 2025-09-25 - [Supabase Pagination N+1 Query Fix]
**Learning:** PostgREST accurately calculates row count while applying filters if the query specifies `count='exact'`. We don't need a separate count query since it ignores `.range()`/.limit()` for the total count return.
**Action:** Append `count='exact'` to the initial `.select("*")` query to get both paginated rows and the total count in a single database roundtrip, then extract the count directly from the result object.
