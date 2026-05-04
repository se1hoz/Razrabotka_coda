import asyncio

async def task(name):
    await asyncio.sleep(1)
    print(name)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    task("Task 1"),
    task("Task 2"),
    task("Task 3")
))
loop.close()