with open('output.txt', 'w', encoding='utf-8') as f:
    f.write("Line 1\nLine 2")

with open('output.txt', 'r', encoding='utf-8') as f:
    print(f.read())