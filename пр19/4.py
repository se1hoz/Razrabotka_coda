import threading
import time

def delayed_task():
    time.sleep(1)
    print(threading.current_thread().name)

thread1 = threading.Thread(target=delayed_task, name="Thread-1")
thread2 = threading.Thread(target=delayed_task, name="Thread-2")
thread3 = threading.Thread(target=delayed_task, name="Thread-3")

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()