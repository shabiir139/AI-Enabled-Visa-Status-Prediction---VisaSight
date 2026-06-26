## 2024-06-26 - Supabase Pagination Optimization
**Learning:** In Supabase/PostgREST, requesting `count='exact'` on the main `select()` query correctly calculates total row count accounting for filters, while ignoring range/limit modifiers. Making a separate query for the total count is an anti-pattern that causes an unnecessary database round-trip.
**Action:** Always append `count='exact'` to the primary query and extract `.count` from the result when implementing paginated list endpoints, eliminating N+1-style metadata queries.
