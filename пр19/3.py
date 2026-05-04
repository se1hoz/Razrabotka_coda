import threading
import time

def print_name():
    print(threading.current_thread().name)

threads = []
for i in range(3):
    t = threading.Thread(target=print_name, name=f"Thread-{i+1}")
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()