with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
unique_lines = dict.fromkeys(line.strip() for line in lines)
with open('unique_lines.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(unique_lines.keys()))
print("Уникальные строки записаны в unique_lines.txt")
