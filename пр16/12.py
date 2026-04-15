import re

def remove_html_tags(text):
    return re.sub(r'<[^>]+>', '', text)

text = "<p>Hello</p>"
print(remove_html_tags(text))
