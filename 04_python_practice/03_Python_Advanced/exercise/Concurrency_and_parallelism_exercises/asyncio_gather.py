import asyncio


async def ok():
    return 1


async def boom():
    raise RuntimeError("x")


async def run_mixed():
    tasks = [ok(), boom()]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results

res = asyncio.run(run_mixed())
assert any(isinstance(x, RuntimeError) for x in res) and 1 in res
print(res)
