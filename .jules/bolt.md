## 2025-05-18 - Single-Query Supabase Pagination Count
**Learning:** Supabase PostgREST allows calculating exact row counts alongside paginated data by appending count='exact' to the primary select query. This avoids a redundant database round-trip for total counts.
**Action:** Always append count='exact' to the select query and read result.count when paginating Supabase queries.
