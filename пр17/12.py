import os

if not os.path.exists('data.txt'):
    with open('data.txt', 'w') as f:
        f.write('Тестовые данные')

if os.path.exists('data.txt'):
    print("Файл data.txt существует")
else:
    print("Файл data.txt не существует")