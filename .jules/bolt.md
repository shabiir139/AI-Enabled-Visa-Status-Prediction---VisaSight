## 2024-07-26 - Single-Trip Supabase Pagination
**Learning:** Supabase Python client's `select` method accepts a `count='exact'` parameter alongside data selection, which correctly calculates total rows matching the filters while ignoring range modifiers.
**Action:** Always combine pagination counts and data fetching into a single Supabase query to avoid redundant round-trips and duplicated filter logic.
