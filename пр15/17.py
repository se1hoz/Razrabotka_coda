import time
from datetime import datetime

now = datetime.now()
timestamp = int(now.timestamp())
print(f"Timestamp: {timestamp}")

back_to_date = datetime.fromtimestamp(timestamp)
print(f"Обратно: {back_to_date}")
