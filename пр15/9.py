with open('result.txt', 'w', encoding='utf-8') as outfile:
    for filename in ['file1.txt', 'file2.txt']:
        with open(filename, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())
            outfile.write('\n')
print("Файлы объединены в result.txt")
