import asyncio
import time


async def rate_limited(ids, *, per_second=5):
    delay = 1.0 / per_second
    last_time = None
    for i in ids:
        now = time.perf_counter()
        if last_time is not None:
            elapsed = now - last_time
            wait = delay - elapsed
            if wait > 0:
                await asyncio.sleep(wait)
        yield i
        last_time = time.perf_counter()


async def test_rate():
    started = time.perf_counter()
    out = [i async for i in rate_limited(range(10), per_second=10)]
    elapsed = time.perf_counter() - started
    assert out == list(range(10))
    assert elapsed >= 1.0/10 * 9 * 0.8  # loose lower bound

asyncio.run(test_rate())
