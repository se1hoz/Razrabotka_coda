import random
import datetime

start = datetime.date(2024, 1, 1)
end = datetime.date(2024, 12, 31)
days_range = (end - start).days

random_days = random.randint(0, days_range)
random_date = start + datetime.timedelta(days=random_days)

print(f"Случайная дата в 2024 году: {random_date.strftime('%d.%m.%Y')}")