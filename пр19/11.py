import multiprocessing
import time

def heavy_math(n):
    result = 0
    for i in range(n):
        result += i ** 2
    return result

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(heavy_math, [1000000, 1000000, 1000000, 1000000])
        print(results)