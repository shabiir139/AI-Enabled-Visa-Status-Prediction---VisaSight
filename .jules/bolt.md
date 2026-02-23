## 2026-02-23 - Pagination Performance
**Learning:** Supabase Python client separates count and data by default if not specified, causing N+1 queries for pagination (one for data, one for count).
**Action:** Always use `.select("*, count='exact'")` for paginated queries to fetch both in a single round-trip.
