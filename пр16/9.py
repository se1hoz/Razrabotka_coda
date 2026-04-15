import re

def is_valid_password(password):
    return len(password) >= 8 and bool(re.search(r'\d', password))

print(is_valid_password("pass1234"))  
print(is_valid_password("pass"))     
