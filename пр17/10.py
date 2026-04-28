import datetime

current = datetime.date.today()
future = current + datetime.timedelta(days=7)
print(f"Текущая дата: {current}")
print(f"Дата + 7 дней: {future}")