## 2024-10-17 - Supabase Pagination Optimization
**Learning:** Supabase Python client's `select("*", count="exact")` retrieves both paginated records and total row count in a single database round-trip. PostgREST calculates the total based on applied filters while ignoring range/limit modifiers. The previous pattern of a separate count query was a codebase-specific anti-pattern that caused N+1 network requests.
**Action:** Always append `count="exact"` to the primary query when implementing pagination to avoid redundant network round-trips.
