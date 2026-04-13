from datetime import datetime

dates = ["2024-12-31", "2023-01-15", "2025-06-01"]
sorted_dates = sorted(dates, key=lambda x: datetime.strptime(x, "%Y-%m-%d"))
print(sorted_dates)

