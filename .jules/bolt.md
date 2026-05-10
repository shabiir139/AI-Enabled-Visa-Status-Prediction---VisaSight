## 2024-05-10 - [Supabase Pagination N+1 Prevention]
**Learning:** [Avoid N+1 redundant queries when using Supabase for pagination. You can supply `count="exact"` to the primary `select("*")` query instead of making a second count query.]
**Action:** [Use `.select("*", count="exact")` for pagination queries and safely extract the count using a fallback pattern like `result.count if hasattr(result, 'count') and result.count is not None else len(result.data)`.]
