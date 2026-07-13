# Proposed Plan

I noticed an N+1 query problem in the backend pagination logic. Currently, when fetching `visa_cases` and `visa_rules`, the application makes two separate requests to Supabase: one to get the paginated records, and another one to get the exact count of the records.

According to the memory: "When implementing pagination with the Supabase client, append `count='exact'` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip. This avoids redundant N+1 queries and prevents bugs where filters are accidentally omitted from a separate count query. PostgREST correctly calculates the total based on applied filters while ignoring range/limit modifiers."

I will implement this optimization in `backend/app/api/cases.py` and `backend/app/api/rules.py` by removing the secondary `count="exact"` query and appending it to the primary `select('*')` query.

## Steps
1. *Modify `backend/app/api/cases.py` to use a single Supabase query for both data and count.*
   - Change `query = supabase.table("visa_cases").select("*")` to `query = supabase.table("visa_cases").select("*", count="exact")`.
   - Remove the separate `count_result` query block.
   - Extract the count using `result.count if hasattr(result, 'count') and result.count is not None else len(result.data)`.
   - Use `replace_with_git_merge_diff` to apply the change.

2. *Modify `backend/app/api/rules.py` to use a single Supabase query for both data and count.*
   - Change `query = supabase.table("visa_rules").select("*").eq("is_active", True)` to `query = supabase.table("visa_rules").select("*", count="exact").eq("is_active", True)`.
   - Remove the separate `count_query` block.
   - Extract the count using `result.count if hasattr(result, 'count') and result.count is not None else len(result.data)`.
   - Use `replace_with_git_merge_diff` to apply the change.

3. *Write to the Bolt journal.*
   - Add an entry to `.jules/bolt.md` documenting the N+1 query optimization using PostgREST's combined select/count functionality to avoid redundant round-trips.
   - Use `run_in_bash_session` to append the entry.

4. *Install backend dependencies and run pytest.*
   - Run `cd backend && pip3 install -r requirements.txt --break-system-packages && pip3 install pytest pytest-asyncio requests httpx<0.28.0 --break-system-packages && PYTHONPATH=. python3 -m pytest` using `run_in_bash_session`.

5. *Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.*

6. *Submit the change.*
   - Use the `submit` tool with branch `bolt-optimize-pagination-queries`, title `⚡ Bolt: Optimize Supabase pagination queries`, and PR description explaining the optimization.
