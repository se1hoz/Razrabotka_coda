import re
from collections import Counter

def count_errors_by_date(logs):
    error_dates = re.findall(r'(\d{4}-\d{2}-\d{2}) ERROR', logs)
    return Counter(error_dates)

logs = """2026-04-01 ERROR Failed
2026-04-01 INFO OK
2026-04-02 ERROR Crash"""

print(count_errors_by_date(logs))

