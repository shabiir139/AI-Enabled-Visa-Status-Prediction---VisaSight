## 2024-07-24 - Combine Supabase select and exact count queries
**Learning:** In Supabase, using `count="exact"` in a `select()` query avoids doing a separate database roundtrip just to count. PostgREST correctly handles this and calculates the total based on applied filters.
**Action:** Always combine pagination counts with the main `select` query by passing `count='exact'` instead of making a separate `.select("id", count="exact")` query.
