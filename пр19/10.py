import threading
import multiprocessing
import time

def cpu_task():
    sum(range(10000000))

def run_threads():
    threads = []
    for _ in range(4):
        t = threading.Thread(target=cpu_task)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def run_processes():
    processes = []
    for _ in range(4):
        p = multiprocessing.Process(target=cpu_task)
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

if __name__ == "__main__":
    start = time.time()
    run_threads()
    print(f"Threads: {time.time() - start:.2f} sec")
    
    start = time.time()
    run_processes()
    print(f"Processes: {time.time() - start:.2f} sec")