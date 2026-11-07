## 2024-11-07 - Supabase exact count optimization
**Learning:** In PostgREST/Supabase, retrieving the total count via a separate query causes a redundant database round-trip (N+1 style problem). Appending `count='exact'` directly to the primary `select('*')` query fetches both the paginated data and the total exact row count in a single request.
**Action:** Use `supabase.table().select('*', count='exact')` and access `result.count` instead of issuing a separate `.select('id', count='exact')` query.
