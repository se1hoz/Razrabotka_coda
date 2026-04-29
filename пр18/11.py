with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("Data for multiple files")

with open('input.txt', 'r', encoding='utf-8') as src, open('copy2.txt', 'w', encoding='utf-8') as dst:
    dst.write(src.read())

print("Файл copy2.txt создан")