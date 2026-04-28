import json

try:
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("Содержимое data.json:")
    print(data)
except FileNotFoundError:
    print("Файл data.json не найден. Сначала запустите 15.py")