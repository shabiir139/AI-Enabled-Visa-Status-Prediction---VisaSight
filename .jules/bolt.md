
## 2024-05-01 - Supabase Single-Roundtrip Pagination
**Learning:** In Supabase, issuing separate `.select("*")` and `.select("id", count="exact")` queries causes unnecessary N+1 query latency patterns. Passing `count="exact"` directly to the data `.select("*")` method performs both operations in one DB request, returning the result list and a `count` property. Note that accessing `result.count` must be checked robustly via `hasattr(result, 'count') and result.count is not None` as the attribute availability can fluctuate depending on empty results or network serialization.
**Action:** Always combine exact pagination counts with data fetches into a single `.select("*", count="exact")` query for all listing operations, and use fallback lengths safely to parse counts.
