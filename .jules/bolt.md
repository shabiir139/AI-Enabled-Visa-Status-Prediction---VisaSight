## 2026-07-01 - Optimize Supabase Pagination Queries
**Learning:** In PostgREST/Supabase, calculating exact total counts via separate N+1 queries is inefficient. Adding `count='exact'` to the primary paginated `select` query fetches both the paginated data and total count in a single database round-trip while correctly respecting filters and ignoring range modifiers.
**Action:** Always append `count='exact'` to the main `select` query instead of issuing separate count queries when implementing pagination.
