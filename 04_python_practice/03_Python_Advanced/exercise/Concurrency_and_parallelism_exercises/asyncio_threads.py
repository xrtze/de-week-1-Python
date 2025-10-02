import asyncio


def cpu_heavy(n):
    """Return sum(i*i for i in range(n)) (CPU-bound)."""
    return sum(i * i for i in range(n))


async def compute_off_thread(n):
    """
    Use asyncio.to_thread(...) (3.9+) to offload cpu_heavy to a thread
    without blocking the event loop. Return the result.
    """
    return await asyncio.to_thread(cpu_heavy, n)

assert asyncio.run(compute_off_thread(10_000)) == sum(
    i*i for i in range(10_000))
