import json

data = {
    "name": "Иван Петров",
    "age": 28,
    "city": "Москва",
    "hobbies": ["чтение", "спорт", "программирование"]
}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Данные сохранены в data.json")