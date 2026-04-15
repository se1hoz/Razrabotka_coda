import re

def find_links(text):
    return re.findall(r'https?://[^\s]+', text)

text = "Visit https://example.com and http://google.com"
print(find_links(text))
