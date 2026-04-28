import random
import datetime
import os

print("=== Полная программа ===\n")

numbers = [random.randint(1, 100) for _ in range(5)]
print(f"1. Случайные числа: {numbers}")

with open('numbers.txt', 'w', encoding='utf-8') as f:
    f.write(f"Дата: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"Числа: {', '.join(map(str, numbers))}\n")

print("2. Сохранено в numbers.txt")

print(f"3. Дата записи: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if os.path.exists('numbers.txt'):
    print("4. Файл numbers.txt существует")
else:
    print("4. Файл numbers.txt не существует")

print("\n5. Содержимое numbers.txt:")
with open('numbers.txt', 'r', encoding='utf-8') as f:
    print(f.read())