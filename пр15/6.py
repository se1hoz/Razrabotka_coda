with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
longest_line = max(lines, key=len)
print(f"Длина: {len(longest_line)}")
print(f"Строка: {longest_line.strip()}")
