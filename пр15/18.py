from datetime import datetime

deadline_str = "2026-04-10"
deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
if datetime.now() > deadline:
    print("Дедлайн просрочен")
else:
    print("Дедлайн ещё не наступил")
