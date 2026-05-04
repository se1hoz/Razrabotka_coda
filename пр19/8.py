import threading
import queue
import time

q = queue.Queue()

def worker():
    while True:
        try:
            task = q.get(timeout=1)
            print(f"{threading.current_thread().name} processing {task}")
            time.sleep(0.5)
            q.task_done()
        except queue.Empty:
            break

for i in range(5):
    q.put(f"Task-{i}")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, name=f"Worker-{i}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()