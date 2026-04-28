import datetime

date1 = datetime.date(2024, 12, 31)
date2 = datetime.date(2024, 1, 1)
diff = (date1 - date2).days
print(f"Разница между 2024-12-31 и 2024-01-01: {diff} дней")