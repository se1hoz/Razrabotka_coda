from datetime import datetime

def log_message(message):
    with open("log_messages.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

log_message("Система запущена")
