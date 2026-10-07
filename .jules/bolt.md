
## 2024-05-18 - Supabase Pagination Redundant Count Queries
**Learning:** When implementing pagination with the Supabase Python client, developers often run a separate query just to get the total count. This results in a redundant N+1 (or 1+1) database query per paginated list request.
**Action:** Always append `count='exact'` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip. The total count can then be safely extracted using `result.count`.
