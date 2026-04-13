with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
count = sum(1 for line in lines if line and line[0].isupper())
print(f"Строк, начинающихся с заглавной буквы: {count}")

with open('result.txt', 'w', encoding='utf-8') as outfile:
    for filename in ['file1.txt', 'file2.txt']:
        with open(filename, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())
            outfile.write('\n')
print("Файлы объединены в result.txt")
