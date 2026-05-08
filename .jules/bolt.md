
## 2024-11-20 - [Supabase N+1 Pagination Optimization]
**Learning:** [When performing paginated queries using Supabase, making a separate call for the count via `.select("id", count="exact")` causes a redundant database round-trip. We can append `count="exact"` directly to the primary data fetch query: `.select("*", count="exact")`. The total count is returned as the `count` attribute of the result object.]
**Action:** [Always combine paginated data fetching and count retrieval into a single Supabase query using `.select("*", count="exact")` to reduce latency and API calls by 50%. Use a fallback structure like `result.count if hasattr(result, "count") and result.count is not None else len(result.data)` for robustness.]
