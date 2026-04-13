import csv

with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    ages = [int(row['age']) for row in reader]
avg_age = sum(ages) / len(ages)
print(f"Средний возраст: {avg_age}")
