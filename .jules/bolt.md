
## 2025-06-06 - Optimize Supabase Pagination Queries
**Learning:** Found an N+1 query problem in the pagination endpoints (`cases.py` and `rules.py`) where fetching data and counting total rows were done in two separate Supabase queries.
**Action:** When implementing pagination with the Supabase client, append `count='exact'` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip, avoiding redundant queries. Provide a fallback pattern like `result.count if hasattr(result, 'count') and result.count is not None else len(result.data)` to handle potential missing attributes robustly.
