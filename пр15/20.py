from collections import defaultdict

errors_by_day = defaultdict(int)
with open('log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if 'ERROR' in line:
            date = line.split()[0]
            errors_by_day[date] += 1
            print(line.strip())  # строки с ERROR

for date, count in sorted(errors_by_day.items()):
    print(f"{date}: {count}")
