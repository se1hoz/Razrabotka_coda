import re

def find_a_words(text):
    return re.findall(r'\b[aA]\w*', text)

text = "Apple and banana are amazing"
print(find_a_words(text))
