## 2026-02-17 - [FastAPI Async vs Sync Blocking]
**Learning:** Defining CPU-bound endpoints (like ML inference) or blocking I/O (like file reads) as `async def` in FastAPI blocks the main event loop, preventing concurrency.
**Action:** Use `def` (synchronous definition) for these endpoints so FastAPI runs them in a thread pool. Ensure shared resources (like ML model loaders) are thread-safe (e.g., using `threading.Lock`).
