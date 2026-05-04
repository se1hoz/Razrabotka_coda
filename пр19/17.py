import asyncio

async def task(delay, name):
    await asyncio.sleep(delay)
    print(f"{name} completed")

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    task(2, "Task 1"),
    task(1, "Task 2"),
    task(3, "Task 3"),
    task(0.5, "Task 4"),
    task(1.5, "Task 5")
))
loop.close()