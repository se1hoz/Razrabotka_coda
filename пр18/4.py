with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("Line 1\nLine 2\nLine 3\nLine 4\nLine 5")

with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')