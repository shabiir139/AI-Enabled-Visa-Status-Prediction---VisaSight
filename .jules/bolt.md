## 2024-05-18 - [Avoid double queries for pagination with Supabase]
**Learning:** Supabase Python client's `select("*", count="exact")` allows retrieving paginated records and the total row count in a single database round-trip. PostgREST correctly calculates the total based on applied filters while ignoring range/limit modifiers.
**Action:** When implementing pagination, always use `count='exact'` in the main query rather than making a second database query for the count.
