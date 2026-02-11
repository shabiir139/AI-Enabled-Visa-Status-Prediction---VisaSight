## 2026-03-03 - [FastAPI Async Blocking]
**Learning:** Using 'async def' for CPU-bound tasks in FastAPI (like ML inference) blocks the main event loop, causing severe latency for concurrent requests.
**Action:** Always use 'def' for CPU-bound endpoints to run them in a thread pool, keeping the event loop responsive.
