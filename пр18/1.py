with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("Hello world!\nPython programming\nThis is a test file")

with open('input.txt', 'r', encoding='utf-8') as f:
    print(f.read())