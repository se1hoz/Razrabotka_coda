import re

def extract_name_age(text):
    match = re.search(r'Name: (\w+) Age: (\d+)', text)
    if match:
        return match.groups()
    return None

text = "Name: John Age: 25"
print(extract_name_age(text))
