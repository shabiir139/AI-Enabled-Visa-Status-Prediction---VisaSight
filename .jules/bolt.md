## 2025-05-25 - [Blocking CPU-bound FastAPI Endpoints]
**Learning:** `async def` path operations in FastAPI run on the main event loop. If the operation is CPU-bound (like ML inference), it blocks the entire server, causing health checks and other requests to time out.
**Action:** Use `def` (instead of `async def`) for CPU-bound endpoints to leverage FastAPI's thread pool, keeping the main event loop responsive.
