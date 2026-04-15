import re

def split_by_comma_space(text):
    return re.split(r'[, ]+', text)

text = "apple, banana orange,grape"
print(split_by_comma_space(text))
