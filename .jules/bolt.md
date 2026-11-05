## 2024-11-05 - Supabase Pagination Optimization
**Learning:** PostgREST can return the exact total row count in a single database round-trip by appending `count='exact'` to the main `select()` query, rather than executing a second count-only query.
**Action:** When implementing pagination with Supabase in Python, avoid double database queries by combining the data fetch and count into a single `select('*', count='exact')` call.
