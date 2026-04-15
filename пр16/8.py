import re

def find_dates(text):
    return re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)

text = "Dates: 2024-01-01 and 2025-12-31"
print(find_dates(text))
