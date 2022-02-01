import re

def fix_price(sup, product):
    return re.sub(f'{sup}\s', " ", product)
