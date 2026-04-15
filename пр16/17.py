import re

def parse_log(line):
    pattern = r'(\d{4}-\d{2}-\d{2}) (INFO|ERROR) (.+)'
    match = re.match(pattern, line)
    if match:
        return match.groups()
    return None

line = "2026-04-01 ERROR Failed"
print(parse_log(line))
