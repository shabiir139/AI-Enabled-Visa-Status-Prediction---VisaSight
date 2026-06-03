## 2025-02-18 - Avoid N+1 Supabase queries
**Learning:** In Supabase, pagination combined with `count="exact"` in a separate query causes unnecessary round trips. It's an N+1 query problem that is easily solved by using `count="exact"` on the primary `select` query.
**Action:** When querying for paginated lists, append `count="exact"` to the primary `select("*")` rather than making a second query just for the count.
