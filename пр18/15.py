import csv

with open('users.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Anna", 25, "Moscow"])
    writer.writerow(["Boris", 30, "SPb"])
    writer.writerow(["Vika", 22, "Kazan"])

with open('users.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)