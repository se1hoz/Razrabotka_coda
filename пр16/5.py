import re

def remove_digits(text):
    return re.sub(r'\d', '', text)

text = "abc123def45"
print(remove_digits(text))
