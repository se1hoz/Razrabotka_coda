import asyncio


async def producer(queue):
    for i in range(5):
        await queue.put(f"Data-{i}")
        print(f"Produced Data-{i}")
        await asyncio.sleep(0.5)


async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumed {item}")
        queue.task_done()


async def main():
    queue = asyncio.Queue()
    prod = asyncio.ensure_future(producer(queue))
    cons = asyncio.ensure_future(consumer(queue))

    await prod
    await queue.join()
    await queue.put(None)
    await cons


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()