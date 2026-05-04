import multiprocessing

def sum_numbers(start, end, result_queue):
    total = sum(range(start, end + 1))
    result_queue.put(total)

if __name__ == "__main__":
    q = multiprocessing.Queue()
    
    p1 = multiprocessing.Process(target=sum_numbers, args=(1, 50000, q))
    p2 = multiprocessing.Process(target=sum_numbers, args=(50001, 100000, q))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    total = q.get() + q.get()
    print(total)