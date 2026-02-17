## 2024-05-23 - FastAPI CPU-Bound Performance
**Learning:** FastAPI endpoints performing heavy CPU-bound tasks (like ML inference) should be defined with `def` instead of `async def`. This ensures they run in a thread pool, preventing the main event loop from being blocked and improving concurrency.
**Action:** Always check `async def` usage in compute-heavy endpoints. If switching to `def`, ensure any shared resources (like global model loaders) are thread-safe using `threading.Lock`.
