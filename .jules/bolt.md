
## 2024-03-26 - Single-Query Pagination Optimization
**Learning:** The synchronous Python Supabase client supports combined data fetching and count retrieval using `.select("*", count="exact")`. The total count is directly accessible via the `count` attribute on the resulting response object (`result.count`). Using this approach instead of a separate count query reduces database roundtrips by 50% for paginated endpoints, addressing a significant architectural bottleneck caused by synchronous I/O.
**Action:** Always use `.select("*", count="exact")` for list endpoints requiring pagination counts to avoid the N+1 query pattern anti-pattern associated with separate count calls in this codebase. Ensure mock data correctly implements both the `data` list and `count` integer attribute.
