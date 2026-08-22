## 2023-10-24 - Supabase Pagination N+1 Query Optimization
**Learning:** Using separate queries for data retrieval and exact count in Supabase pagination leads to unnecessary database round-trips and potential bugs if filters are mismatched.
**Action:** Always append count='exact' to the primary select('*') query to retrieve both paginated records and the total row count in a single database round-trip.
