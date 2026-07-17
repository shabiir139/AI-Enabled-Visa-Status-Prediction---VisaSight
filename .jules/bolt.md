## 2024-05-15 - Optimize Supabase Pagination Count
**Learning:** Supabase PostgREST allows fetching exact counts alongside data in a single query by using `select("*", count="exact")`. It correctly calculates the total count based on filters while ignoring range limits.
**Action:** Always append `count="exact"` to the primary `select` query when paginating to avoid redundant N+1 queries.

## 2024-05-15 - Fast API Dependencies Issue
**Learning:** Some python testing scripts ran quickly because FastAPI imports were successful locally on my machine, but failed in an isolated CI container because `fastapi` was not correctly listed as installed due to environment scoping. Re-running pip install with `--break-system-packages` successfully fixed it and verified tests passed correctly.
**Action:** Be mindful of python environment states when testing CI steps and ensure the full requirement stack is loaded successfully.
