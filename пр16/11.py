import re

def replace_short_words(text):
    return re.sub(r'\b\w{1,2}\b', '****', text)

print(replace_short_words("a cat and dog go"))
