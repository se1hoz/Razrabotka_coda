import threading
import time

def daemon_task():
    while True:
        print("Daemon is running")
        time.sleep(2)

daemon = threading.Thread(target=daemon_task, daemon=True)
daemon.start()

time.sleep(5)
print("Main program exiting")