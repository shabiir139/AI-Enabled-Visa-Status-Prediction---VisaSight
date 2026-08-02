## 2026-03-01 - [Optimize Supabase Count Queries]
**Learning:** The python supabase client permits passing `count='exact'` directly to the `.select()` query in order to simultaneously perform paginated selections and grab total count in a single round trip to reduce network calls.
**Action:** When doing paginated queries with Supabase, append `count='exact'` instead of running a duplicate query just to fetch count.
