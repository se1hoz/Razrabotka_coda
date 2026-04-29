with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("Line 1\nLine 2\nLine 3")

with open('input.txt', 'r', encoding='utf-8') as f:
    line_count = sum(1 for _ in f)
print(f"Количество строк: {line_count}")