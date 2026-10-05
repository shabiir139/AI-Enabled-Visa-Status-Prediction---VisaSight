## 2024-05-30 - Supabase Single Query Pagination
**Learning:** When paginating with Supabase client, performing a separate `count` query introduces N+1 performance issues (two database round-trips instead of one) and can lead to bugs where filters diverge between the data query and the count query.
**Action:** Always append `count='exact'` (or `'estimated'`) to the primary `.select()` query. Supabase/PostgREST correctly calculates the total count based on applied filters while ignoring range limits, eliminating the need for a separate database call.
