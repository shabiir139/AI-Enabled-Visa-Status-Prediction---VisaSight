## 2026-09-15 - Optimize Supabase Count Queries
**Learning:** When implementing pagination with the Supabase client, the Python client allows appending `count='exact'` to the primary `select('*')` query to retrieve both paginated records and the total row count in a single database round-trip. This avoids redundant N+1 queries.
**Action:** Combine the main query and the count query into a single Supabase query call in backend pagination endpoints like `api/cases.py` and `api/rules.py`.
## 2026-09-15 - Fix CI Workflow Paths
**Learning:** When modifying GitHub Actions CI workflows (e.g., `.github/workflows/ci.yml`), ensure the `working-directory` and `cache-dependency-path` values are correctly set to the root `./backend` and `./frontend` directories (e.g., `./frontend/package-lock.json`), rather than using incorrect nested structures (like `visasight/frontend`), to prevent 'No such file or directory' or 'unable to cache dependencies' errors in the CI runners.
**Action:** Update the CI workflow file to use correct paths without the `visasight/` prefix, and update node versions to avoid deprecation warnings.
