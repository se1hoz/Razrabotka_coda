import re

def is_ipv4(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(pattern, ip):
        return False
    for part in ip.split('.'):
        if not 0 <= int(part) <= 255:
            return False
    return True

print(is_ipv4("192.168.1.1"))
print(is_ipv4("256.1.1.1"))
