## 2024-05-24 - Supabase Pagination Optimization
**Learning:** In the Supabase Python client, we can retrieve both paginated records and the total row count in a single database round-trip by passing `count='exact'` to the primary `select()` query. This avoids a common anti-pattern of making a separate request just to calculate totals, which wastes a network round-trip.
**Action:** When implementing pagination in Supabase, always append `count='exact'` to the primary `select()` query to retrieve both the items and total count simultaneously, rather than performing two separate API calls.
