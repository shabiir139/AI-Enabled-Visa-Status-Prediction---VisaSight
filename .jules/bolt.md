## 2023-10-04 - [Supabase Python Client Pagination Optimization]
**Learning:** PostgREST API (which Supabase uses) supports combined pagination and exact counting in a single round-trip by passing `count="exact"` into the `select()` statement.
**Action:** Always append `count="exact"` to the primary `select('*')` query when retrieving paginated records using the Supabase client to avoid N+1 queries. Access the count via `result.count` and fallback gracefully if it is None or missing.
