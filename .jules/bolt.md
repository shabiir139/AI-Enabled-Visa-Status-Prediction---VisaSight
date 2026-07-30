## 2024-05-30 - [Performance: N+1 query and pagination]
**Learning:** Found N+1 query issue in Supabase pagination logic in `backend/app/api/cases.py`. `count_result = supabase.table("visa_cases").select("id", count="exact")` does a completely separate query just for the count.
**Action:** Append `count='exact'` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip. This avoids redundant N+1 queries.
