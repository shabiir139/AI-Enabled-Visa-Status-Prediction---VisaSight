## 2025-05-18 - [Fix main thread blocking and N+1 queries]
**Learning:** Using `async def` for FastAPI endpoints doing synchronous database requests (e.g. `supabase-py`'s `.execute()`) or CPU-bound ML inference blocks the main event loop, significantly degrading concurrent performance. FastAPI runs synchronous `def` endpoints in an external threadpool. Additionally, `supabase-py` supports `.select('*', count='exact')` allowing data and total count to be retrieved in a single query, thus preventing N+1/duplicate query issues for pagination endpoints.
**Action:** When creating new FastAPI endpoints involving synchronous operations (like `supabase-py`), declare them with `def` rather than `async def`. For pagination, fetch data and total count simultaneously using `count='exact'` in the `select()` call to avoid multiple queries.

## 2025-05-18 - [Fix CI workflow paths]
**Learning:** The GitHub Actions workflow (`.github/workflows/ci.yml`) failed because it was incorrectly looking for `visasight/frontend` and `visasight/backend` directories. The repository is a flat monorepo with `frontend` and `backend` at the root.
**Action:** When updating or working with GitHub Actions workflows in this repository, ensure `working-directory` and path configs (like `cache-dependency-path`) point to `./frontend` or `./backend`, not `./visasight/frontend` or `./visasight/backend`.

## 2025-05-18 - [Fix Next.js strict linting errors]
**Learning:** Next.js enforces strict React linting rules, including `react/no-unescaped-entities` which fails the CI build if unescaped single quotes are used in JSX (e.g., `'` instead of `&apos;`). Additionally, `react-hooks/exhaustive-deps` will cause warnings (or errors in strict mode) if functions called inside `useEffect` are not wrapped in `useCallback` or included in the dependency array.
**Action:** When adding or modifying text in JSX, always use HTML entities like `&apos;` for apostrophes. When defining functions that are called within `useEffect`, either define them inside the effect or wrap them in `useCallback` and include them in the dependency array.
