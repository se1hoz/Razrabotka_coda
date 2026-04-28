import os

if not os.path.exists('data.txt'):
    with open('data.txt', 'w') as f:
        f.write('Тестовое содержимое для проверки размера')

size = os.path.getsize('data.txt')
print(f"Размер файла data.txt: {size} байт")