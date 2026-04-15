import re

def mask_card_number(card):
    return re.sub(r'\d(?=\d{4})', '*', card)

print(mask_card_number("1234 5678 9012 3456"))
