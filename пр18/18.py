with open('log.txt', 'w', encoding='utf-8') as f:
    f.write("[2024-01-01 10:00:00] INFO: Started\n")
    f.write("[2024-01-01 10:01:00] ERROR: Connection failed\n")
    f.write("[2024-01-01 10:02:00] INFO: Retrying\n")
    f.write("[2024-01-01 10:03:00] ERROR: Timeout\n")
    f.write("[2024-01-01 10:04:00] ERROR: Disk full\n")

with open('log.txt', 'r', encoding='utf-8') as f:
    error_count = sum(1 for line in f if "ERROR" in line)
print(f"Количество строк с ERROR: {error_count}")