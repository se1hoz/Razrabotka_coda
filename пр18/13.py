with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("First line\nSecond line\nThird line")

with open('input.txt', 'r', encoding='utf-8') as src, open('numbered.txt', 'w', encoding='utf-8') as dst:
    for i, line in enumerate(src, 1):
        dst.write(f"{i}: {line}")

print("Файл numbered.txt создан")