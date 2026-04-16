## 2024-05-24 - [Combine Supabase pagination queries for faster loading]
**Learning:** Avoid using two separate `.execute()` calls for fetching paginated data and the total count. Using `.select("*", count="exact")` allows fetching both the paginated data and the exact total count in a single query database round-trip. Ensure the extracted count falls back gracefully to `len(result.data)` in cases where `count` attribute might be missing.
**Action:** Always combine pagination data and count queries into a single `.select("*", count="exact")` execution when working with the Supabase client.
