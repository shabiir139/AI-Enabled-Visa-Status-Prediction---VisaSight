
## 2026-08-29 - Prevent redundant count queries in Supabase pagination
**Learning:** Supabase Python client can retrieve both paginated records and the total row count in a single database round-trip using `select('*', count='exact')`. PostgREST calculates the total based on filters, ignoring range/limit modifiers. Doing a separate `select('id', count='exact')` causes unnecessary N+1 queries or extra round trips.
**Action:** When implementing pagination with the Supabase client, append `count='exact'` to the primary `select('*')` query to retrieve both records and total count in a single network request.
