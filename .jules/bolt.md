## 2025-02-23 - Supabase Count Query Optimization
**Learning:** Supabase Python client (postgrest) supports retrieving the total count alongside data in a single query using `count="exact"`. The count is available as a property on the result object (`result.count`).
**Action:** When implementing pagination or list views that require a total count, always use `count="exact"` in the initial query instead of making a separate request to count rows.
