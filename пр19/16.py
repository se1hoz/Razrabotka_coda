import asyncio

async def task(delay, name):
    await asyncio.sleep(delay)
    return name

loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(
    task(2, "First"),
    task(1, "Second"),
    task(3, "Third")
))
print(results)
loop.close()