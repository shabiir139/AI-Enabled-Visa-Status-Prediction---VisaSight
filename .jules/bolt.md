## 2025-02-27 - [Supabase Count Pagination]
**Learning:** Using separate queries for retrieving data and counting rows in Supabase Python Client causes an unnecessary database round-trip.
**Action:** Use `select("*", count="exact")` in the primary query and read `result.count` to avoid a separate count query. Handle `None` gracefully.
