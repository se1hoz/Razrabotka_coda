from datetime import datetime, timedelta

def next_monday(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    days_ahead = (7 - date.weekday()) % 7
    if days_ahead == 0:
        days_ahead = 7
    return date + timedelta(days=days_ahead)

print(next_monday("2024-12-31"))
