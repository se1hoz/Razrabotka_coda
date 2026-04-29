with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("hello world\npython programming")

with open('input.txt', 'r', encoding='utf-8') as src:
    content = src.read()

with open('upper.txt', 'w', encoding='utf-8') as dst:
    dst.write(content.upper())

print("Файл upper.txt создан")