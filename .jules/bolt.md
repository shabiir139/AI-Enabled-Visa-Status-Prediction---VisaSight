
## 2024-04-18 - Supabase Exact Count Pagination Pattern
**Learning:** Calling Supabase `.select("id", count="exact")` directly after a standard `.select("*")` query is a redundant network hop. Supabase allows combining these operations into a single `.select("*", count="exact")` call, which populates both `result.data` and `result.count` in a single response, effectively halving the latency of paginated endpoints.
**Action:** When implementing pagination with the Supabase Python client, always use `.select("*", count="exact")` and extract the total count via `result.count`. Provide appropriate fallback logic (`if hasattr(result, 'count') and result.count is not None else len(result.data)`) to handle edge cases safely.
