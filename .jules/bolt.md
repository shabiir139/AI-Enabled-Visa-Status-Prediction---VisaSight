## 2025-01-20 - [Supabase Single-Trip Pagination]
**Learning:** Supabase / PostgREST correctly computes total dataset size with `count="exact"` in the primary `select` query while simultaneously returning paginated results based on range/limit. Doing separate count queries is redundant and wastes a DB round trip.
**Action:** Always append `count="exact"` to the primary `select` when fetching paginated sets and extract it via `result.count` instead of issuing a second parallel or sequential query.
