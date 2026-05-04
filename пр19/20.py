import asyncio
import time


class TaskSystem:
    def __init__(self, num_workers):
        self.queue = asyncio.Queue()
        self.workers = num_workers
        self.results = []

    async def worker(self, wid):
        while True:
            try:
                task = await asyncio.wait_for(self.queue.get(), timeout=1)
                print(f"Worker {wid} started task {task['id']}")
                await asyncio.sleep(task['duration'])
                print(f"Worker {wid} completed task {task['id']}")
                self.results.append({**task, 'status': 'done', 'worker': wid})
                self.queue.task_done()
            except asyncio.TimeoutError:
                break

    async def add_task(self, tid, duration):
        await self.queue.put({'id': tid, 'duration': duration})
        print(f"Task {tid} added to queue")

    async def run(self, tasks):
        for t in tasks:
            await self.add_task(t[0], t[1])

        workers = [asyncio.ensure_future(self.worker(i)) for i in range(self.workers)]
        await self.queue.join()

        for w in workers:
            w.cancel()

        return self.results


async def main():
    system = TaskSystem(3)
    tasks = [("T1", 1), ("T2", 0.5), ("T3", 1.5), ("T4", 0.8), ("T5", 1.2)]
    results = await system.run(tasks)
    print(f"Completed {len(results)} tasks")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()