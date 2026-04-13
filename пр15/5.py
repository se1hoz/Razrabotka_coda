import csv
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
with open('filtered.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age'])
    writer.writeheader()
    writer.writerows([row for row in rows if int(row['age']) > 25])
print("Отфильтрованные строки записаны в filtered.csv")
