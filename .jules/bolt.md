## 2023-10-27 - Supabase Pagination Optimization
**Learning:** Supabase Python client can fetch both paginated data and the exact total count in a single query by appending `count="exact"` to the primary `select("*")` method. This avoids the N+1 query anti-pattern of running a separate `select("id", count="exact")` query for pagination metadata.
**Action:** Always combine pagination data fetches and count fetches into a single Supabase query to reduce database round-trips and improve latency.
