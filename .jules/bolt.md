## 2026-09-15 - Optimize Supabase Count Queries
**Learning:** When implementing pagination with the Supabase client, the Python client allows appending `count='exact'` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip. This avoids redundant N+1 queries.
**Action:** Combine the main query and the count query into a single Supabase query call in backend pagination endpoints like `api/cases.py` and `api/rules.py`.
