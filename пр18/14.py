with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("Line 1\n\nLine 2\n\n\nLine 3")

with open('input.txt', 'r', encoding='utf-8') as src, open('no_empty.txt', 'w', encoding='utf-8') as dst:
    for line in src:
        if line.strip():
            dst.write(line)

print("Файл no_empty.txt создан")