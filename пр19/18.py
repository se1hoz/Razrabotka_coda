import asyncio

async def read_file(filename):
    print(f"Reading {filename}")
    await asyncio.sleep(1)
    print(f"Finished reading {filename}")
    return f"Content of {filename}"

loop = asyncio.get_event_loop()
files = ["file1.txt", "file2.txt", "file3.txt"]
tasks = [read_file(f) for f in files]
results = loop.run_until_complete(asyncio.gather(*tasks))
for r in results:
    print(r)
loop.close()