## 2024-05-22 - [FastAPI Async vs Sync for ML]
**Learning:** ML inference is CPU bound and blocks the main event loop if run in `async def` endpoints. Changing to `def` runs them in a thread pool, but requires thread safety in shared resources (like model loading).
**Action:** Always verify if an endpoint is CPU bound or I/O bound. Use `def` for CPU bound tasks in FastAPI and ensure thread safety for global objects.
