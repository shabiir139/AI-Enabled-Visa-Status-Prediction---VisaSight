1. **Identify Performance Bottleneck**: The Supabase pagination queries in `backend/app/api/cases.py` and `backend/app/api/rules.py` execute two separate database calls: one for paginated rows and another for the total count. This doubles database latency for these endpoints and is prone to synchronization errors if filters get mismatched.
2. **Optimize `backend/app/api/cases.py`**:
   - Replace the two `supabase.table("visa_cases").select(...)` queries with a single query using `select("*", count="exact")`.
   - Update code via `replace_with_git_merge_diff`.
3. **Optimize `backend/app/api/rules.py`**:
   - Replace the two `supabase.table("visa_rules").select(...)` queries with a single query using `select("*", count="exact")`.
   - Update code via `replace_with_git_merge_diff`.
4. **Log Learning**:
   - Write an entry to `.jules/bolt.md` documenting the N+1 anti-pattern found in Supabase queries and the single query solution.
5. **Install Dependencies & Test**:
   - Install backend dependencies with `python3 -m pip install -r backend/requirements.txt --break-system-packages` and testing libs `python3 -m pip install pytest pytest-asyncio requests --break-system-packages`.
   - Start the backend server and run `python3 backend/quick_model_test.py`.
   - Run backend tests using `python3 -m pytest backend/`.
6. **Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done**.
7. **Submit Changes**: Submit using `submit` with branch `bolt/optimize-supabase-pagination`, describing the ~50% latency reduction by dropping redundant db queries.
