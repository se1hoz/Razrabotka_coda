from datetime import datetime, timedelta
def workdays_between(date1, date2):
    start = datetime.strptime(date1, "%Y-%m-%d")
    end = datetime.strptime(date2, "%Y-%m-%d")
    days = 0
    current = start
    while current <= end:
        if current.weekday() < 5:  # 0=пн, 4=пт
            days += 1
        current += timedelta(days=1)
    return days

# Пример
print(workdays_between("2024-12-01", "2024-12-10"))
