## 2024-09-20 - Optimize Pagination Database Queries
**Learning:** The Supabase Python client can retrieve both paginated records and the total row count in a single database round-trip by appending `count="exact"` to the primary `select("*")` query, which natively handles filtering while ignoring range modifiers.
**Action:** Always append `count="exact"` to the primary pagination query instead of executing a secondary query just for the count, to reduce database queries and prevent filter mismatch bugs.
