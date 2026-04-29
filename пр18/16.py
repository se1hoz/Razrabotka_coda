import datetime

with open('log.txt', 'w', encoding='utf-8') as f:
    pass

log_message = "Test log message"
current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('log.txt', 'a', encoding='utf-8') as f:
    f.write(f"[{current_time}] {log_message}\n")

print("Лог записан в log.txt")