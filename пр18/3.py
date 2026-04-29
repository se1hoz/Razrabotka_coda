with open('output.txt', 'w', encoding='utf-8') as f:
    f.write("Hello, world!")

with open('output.txt', 'a', encoding='utf-8') as f:
    f.write("\nPython")

with open('output.txt', 'r', encoding='utf-8') as f:
    print(f.read())