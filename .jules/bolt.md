## 2024-11-09 - Combine Supabase Queries for Pagination
**Learning:** Supabase Python client allows combining data fetch and exact row count in a single database round-trip by passing `count="exact"` to the primary `select()` query, which PostgREST correctly handles alongside `.range()` pagination modifiers.
**Action:** Append `count='exact'` to the main query and extract `total = result.count if hasattr(result, 'count') and result.count is not None else len(result.data)` instead of issuing a separate `select("id", count="exact")` query.
