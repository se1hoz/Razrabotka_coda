import csv

try:
    with open('users.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        print("Содержимое users.csv:")
        for row in reader:
            print(f"  {row}")
except FileNotFoundError:
    print("Файл users.csv не найден. Сначала запустите 17.py")