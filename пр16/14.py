import re

def find_duplicate_words(text):
    return re.findall(r'\b(\w+)\s+\1\b', text)

text = "hello hello world"
print(find_duplicate_words(text))
