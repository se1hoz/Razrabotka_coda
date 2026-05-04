import threading
import time

def download_file(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Finished {name}")

files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]

threads = []
for f in files:
    t = threading.Thread(target=download_file, args=(f,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()