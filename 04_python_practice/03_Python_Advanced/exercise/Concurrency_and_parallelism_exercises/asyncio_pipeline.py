import asyncio
from typing import Optional, Dict


async def parse(line: str) -> Optional[Dict[str, int]]:
    """Parse 'key:value' lines; return {'key': key, 'value': int(value)} or None."""
    try:
        key, val = line.split(":", 1)
        return {"key": key.strip(), "value": int(val.strip())}
    except Exception:
        return None


async def transform(rec: Dict[str, int]) -> Dict[str, int]:
    """Return rec with value doubled (simulate I/O with small sleep)."""
    await asyncio.sleep(0.01)  # simulate async I/O
    return {"key": rec["key"], "value": rec["value"] * 2}


async def aggregate(lines: list[str]) -> Dict[str, int]:
    """
    Use asyncio tasks + Semaphore to fan out parse/transform and then
    aggregate totals per key. Return dict key->total.
    """
    sem = asyncio.Semaphore(5)  # limit concurrency

    async def worker(line: str) -> Optional[Dict[str, int]]:
        async with sem:
            parsed = await parse(line)
            if parsed is None:
                return None
            transformed = await transform(parsed)
            return transformed

    tasks = [asyncio.create_task(worker(line)) for line in lines]
    results = await asyncio.gather(*tasks)

    totals = {}
    for res in results:
        if res is None:
            continue
        totals[res["key"]] = totals.get(res["key"], 0) + res["value"]
    return totals

res = asyncio.run(aggregate(["a:1", "b:2", "bad", "a:3"]))
assert res == {"a": 8, "b": 4}
print(res)
