import re

def is_latvian_phone(number):
    return bool(re.match(r'^\+371\d{8}$', number))

text = "+37112345678"
print(is_latvian_phone(text))
