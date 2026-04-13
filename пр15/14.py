from datetime import datetime

birth = input("Введите дату рождения (ГГГГ-ММ-ДД): ")
birth_date = datetime.strptime(birth, "%Y-%m-%d")
age_days = (datetime.now() - birth_date).days
print(f"Возраст в днях: {age_days}")
