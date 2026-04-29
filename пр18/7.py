with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("This is content for copying")

with open('input.txt', 'r', encoding='utf-8') as src:
    with open('copy.txt', 'w', encoding='utf-8') as dst:
        dst.write(src.read())

print("Файл copy.txt создан")