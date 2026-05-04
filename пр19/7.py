import threading
import queue
import time

q = queue.Queue()

def producer():
    for i in range(5):
        q.put(f"Task-{i}")
        time.sleep(0.1)

def consumer():
    while True:
        try:
            item = q.get(timeout=1)
            print(f"Processing {item}")
            q.task_done()
        except queue.Empty:
            break

prod = threading.Thread(target=producer)
cons = threading.Thread(target=consumer)

prod.start()
cons.start()

prod.join()
cons.join()