## 2024-05-30 - N+1 Query in Supabase Client for Pagination
**Learning:** Found a performance bottleneck where paginated list endpoints (`/api/cases`, `/api/rules`) make two separate requests to Supabase: one to fetch data using `.range()` and another to fetch the total count. This doubles the network latency and database round-trips unnecessarily.
**Action:** Append `count='exact'` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip. The Python Supabase client supports this via `.select('*', count='exact')`.
