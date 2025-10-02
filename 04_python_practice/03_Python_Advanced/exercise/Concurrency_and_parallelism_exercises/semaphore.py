import asyncio
import random


async def fetch_one(i: int):
    """Simulate I/O by sleeping random small time, then return i."""
    await asyncio.sleep(0.01 + random.random()*0.02)
    return i


async def gather_limited(n, limit):
    sem = asyncio.Semaphore(limit)

    async def sem_task(i):
        async with sem:
            return await fetch_one(i)

    tasks = [asyncio.create_task(sem_task(i)) for i in range(n)]
    results = await asyncio.gather(*tasks)
    return results

out = asyncio.run(gather_limited(10, 3))
assert sorted(out) == list(range(10))
print(out)
