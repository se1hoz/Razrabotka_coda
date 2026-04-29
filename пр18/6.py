with open('input.txt', 'w', encoding='utf-8') as f:
    f.write("Hello world Python programming")

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    word_count = len(text.split())
print(f"Количество слов: {word_count}")