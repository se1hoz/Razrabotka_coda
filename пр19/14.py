import asyncio

async def simple_task():
    await asyncio.sleep(1)
    print("Task completed")

loop = asyncio.get_event_loop()
loop.run_until_complete(simple_task())
loop.close()