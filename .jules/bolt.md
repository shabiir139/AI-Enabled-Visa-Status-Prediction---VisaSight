## 2024-09-10 - Supabase Single Round-Trip Pagination
**Learning:** Using `count="exact"` in the primary `.select()` query in python Supabase client gets the count and limits pagination correctly, avoiding N+1 query issue for counts.
**Action:** Always append `count='exact'` to the primary `select()` query when pagination and total count are required to optimize database round-trips.
