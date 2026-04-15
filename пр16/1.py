import re

def has_python(text):
    return bool(re.search(r'Python', text))

text = "I love Python programming"
print(has_python(text))
