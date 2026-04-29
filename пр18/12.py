with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("Hi\nHello world\nPython\nShort\nLong line here")

with open('input.txt', 'r', encoding='utf-8') as src, open('filtered.txt', 'w', encoding='utf-8') as dst:
    for line in src:
        if len(line.strip()) > 5:
            dst.write(line)

print("Файл filtered.txt создан")