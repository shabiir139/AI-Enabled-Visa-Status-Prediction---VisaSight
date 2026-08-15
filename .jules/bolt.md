## 2024-05-19 - N+1 Supabase queries
**Learning:** Found N+1 query problem with Supabase in backend/app/api/cases.py and backend/app/api/rules.py where pagination is done with two requests: one for records and one for count.
**Action:** Use supabase select with `count="exact"` on the primary data fetch to get both paginated records and total count in a single round-trip.
