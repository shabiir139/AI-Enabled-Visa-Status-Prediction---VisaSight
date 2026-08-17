## 2024-08-17 - Supabase count exact with main query
**Learning:** Appending `count="exact"` to the primary `select("*")` query eliminates the need for a separate count query, halving the database round-trips for paginated endpoints.
**Action:** Use `.select("*", count="exact")` instead of running two separate `.select("*")` and `.select("id", count="exact")` queries when fetching paginated lists with Supabase.
