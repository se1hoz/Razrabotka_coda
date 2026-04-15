import re

def capitalize_words(text):
    return re.sub(r'\b\w', lambda m: m.group(0).upper(), text)

print(capitalize_words("hello world python"))
