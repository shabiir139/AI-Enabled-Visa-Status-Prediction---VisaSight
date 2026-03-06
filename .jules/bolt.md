## 2024-03-06 - [Supabase Pagination Optimization]
**Learning:** [Combining `.select('*', count='exact')` in the Supabase Python client fetches both the result set and the total exact count in a single query. This removes the necessity of initiating a secondary query strictly to obtain the count for pagination, thus practically cutting latency in half for these types of list endpoints.]
**Action:** [Always append `count='exact'` to `.select()` queries that retrieve a subset of data but still require presenting a total count, such as for pagination.]
