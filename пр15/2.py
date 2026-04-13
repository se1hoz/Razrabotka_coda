from collections import Counter
import re

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()
words = re.findall(r'\b\w+\b', text.lower())
word_counts = Counter(words)
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words:
    print(f"{word}: {count}")