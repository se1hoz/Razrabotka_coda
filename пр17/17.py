import csv

users = [
    ["Имя", "Возраст", "Город", "Email"],
    ["Анна Смирнова", 25, "СПб", "anna@mail.ru"],
    ["Борис Кузнецов", 32, "Москва", "boris@mail.ru"],
    ["Виктория Лебедева", 29, "Казань", "vika@mail.ru"],
    ["Дмитрий Соколов", 35, "Новосибирск", "dima@mail.ru"]
]

with open('users.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(users)

print("CSV файл users.csv создан")