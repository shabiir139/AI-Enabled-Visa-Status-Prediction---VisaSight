
## 2024-04-05 - Supabase Pagination Single Query
**Learning:** In the Supabase Python SDK, executing a data fetch (`select("*")`) and a separate count query (`select("id", count="exact")`) for paginated lists essentially doubles the database latency by making two network calls. The SDK supports an undocumented optimization where `.select('*', count='exact')` will retrieve both the requested paginated rows and the total unpaginated exact count in a single network request. The count is exposed directly on the response object (`result.count`).
**Action:** Always combine pagination data fetches and count queries into a single `.select('*', count='exact')` call for backend endpoints, extracting `count` safely with a fallback to `len(result.data)` if missing.
