
## 2026-08-29 - Prevent redundant count queries in Supabase pagination
**Learning:** Supabase Python client can retrieve both paginated records and the total row count in a single database round-trip using `select('*', count='exact')`. PostgREST calculates the total based on filters, ignoring range/limit modifiers. Doing a separate `select('id', count='exact')` causes unnecessary N+1 queries or extra round trips.
**Action:** When implementing pagination with the Supabase client, append `count='exact'` to the primary `select('*')` query to retrieve both records and total count in a single network request.

## 2026-08-29 - GitHub Actions Working Directory Fix
**Learning:** When configuring GitHub Actions for a monorepo setup, specifying a non-existent parent directory like `visasight/` in `working-directory` or `cache-dependency-path` causes step failures (e.g., 'No such file or directory', 'unable to cache dependencies'). Ensure paths exactly match the repository root structure.
**Action:** Verify the exact directory names relative to the repository root before setting them in CI workflow configurations.
