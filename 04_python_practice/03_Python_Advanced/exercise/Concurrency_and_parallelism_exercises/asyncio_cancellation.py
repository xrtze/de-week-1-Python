import asyncio


async def sleepy():
    try:
        await asyncio.sleep(1)
        return "done"
    finally:
        # cleanup code runs even if cancelled
        print("Cleanup running")


async def cancel_demo():
    task = asyncio.create_task(sleepy())
    await asyncio.sleep(0.05)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        return "cancelled"

assert asyncio.run(cancel_demo()) == "cancelled"
