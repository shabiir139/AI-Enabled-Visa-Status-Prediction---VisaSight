## 2024-05-24 - Supabase pagination with single query
**Learning:** Supabase Python client can retrieve the total row count along with paginated records in a single database round-trip by passing `count='exact'` to `select()`, avoiding a separate N+1 query for the count.
**Action:** When implementing pagination with Supabase, append `count='exact'` to the primary `select` query and extract the count from the initial result rather than performing a separate database call.
