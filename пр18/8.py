import os

with open('input.txt', 'w', encoding='utf-8') as f:
    pass

if os.path.getsize('input.txt') == 0:
    print("Empty")
else:
    print("Файл не пуст")