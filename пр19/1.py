import time

def task1():
    for i in range(1, 4):
        print(f"Task1 - строка {i}")
        time.sleep(0.1)

def task2():
    for i in range(1, 4):
        print(f"Task2 - строка {i}")
        time.sleep(0.1)

print("Последовательное выполнение:")
task1()
task2()

print("\nПсевдопараллельное выполнение:")
for i in range(1, 4):
    print(f"Task1 - строка {i}")
    print(f"Task2 - строка {i}")
    time.sleep(0.1)