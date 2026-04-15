import re

def find_numbers(text):
    return re.findall(r'\d+', text)

text = "There are 12 apples and 5 bananas"
print(find_numbers(text))

