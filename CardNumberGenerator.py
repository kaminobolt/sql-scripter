import re
import random

regex = re.compile("^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})$")

def is_cardnumber(card_num):
    if re.match(regex, card_num) == None:
        return False
    else:
        return True

def card_num_gen():
     return random.randrange(4000000000000000, 6000000000000000, 1)


