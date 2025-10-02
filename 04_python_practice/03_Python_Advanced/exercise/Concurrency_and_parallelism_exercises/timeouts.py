import asyncio


async def maybe_slow(dt):
    await asyncio.sleep(dt)
    return dt


async def with_timeout(dt, timeout):
    return await asyncio.wait_for(maybe_slow(dt), timeout=timeout)

# Tests
ok = asyncio.run(with_timeout(0.01, 0.1))
assert ok == 0.01

try:
    asyncio.run(with_timeout(0.2, 0.05))
    assert False, "should timeout"
except asyncio.TimeoutError:
    pass
