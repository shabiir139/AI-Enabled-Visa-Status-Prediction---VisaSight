## 2025-02-09 - N+1 Supabase Query Optimization
**Learning:** Found a N+1 query issue in Supabase pagination logic in `backend/app/api/cases.py` and `backend/app/api/rules.py` where a separate count query is being performed instead of chaining `count="exact"` on the same paginated query.
**Action:** Use `select("*", count="exact")` directly on the main query for pagination to avoid a second database round-trip for calculating `total`.
