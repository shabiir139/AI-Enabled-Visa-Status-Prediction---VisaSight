## 2025-10-31 - Supabase N+1 Pagination Optimization
**Learning:** Found N+1 queries during Supabase pagination in `backend/app/api/cases.py` and `backend/app/api/rules.py` where a separate count query is made after fetching records.
**Action:** Use `count='exact'` in the main data retrieval query using `select('*', count='exact')` to get both the data and total count in a single round-trip.
