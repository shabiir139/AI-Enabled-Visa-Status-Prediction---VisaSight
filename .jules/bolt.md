## 2025-02-09 - N+1 Supabase Query Optimization
**Learning:** Found a N+1 query issue in Supabase pagination logic in `backend/app/api/cases.py` and `backend/app/api/rules.py` where a separate count query is being performed instead of chaining `count="exact"` on the same paginated query.
**Action:** Use `select("*", count="exact")` directly on the main query for pagination to avoid a second database round-trip for calculating `total`.

## 2025-02-09 - CI Path Error
**Learning:** The GitHub actions CI file `.github/workflows/ci.yml` had incorrect `working-directory` configuration pointing to `./visasight/frontend` and `./visasight/backend` when the repo root is actually the parent folder, so it should be just `./frontend` and `./backend`.
**Action:** Modify `ci.yml` to remove the incorrect `visasight/` prefix from all path configurations.
