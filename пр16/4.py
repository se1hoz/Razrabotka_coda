import re

def replace_spaces(text):
    return re.sub(r' ', '_', text)

text = "Hello world Python"
print(replace_spaces(text))
