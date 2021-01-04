#!/usr/bin/python

import re
import sys
import random

regex = re.compile("^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})$")
card_limit = int(sys.argv[1])
n = 0
rows = 0

print("CREATE TABLE CARDDATA (a, b, c, d, e);")


def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0

def is_cardnumber(card_num):
    if re.match(regex, card_num) == None:
        return False
    else:
        return True



while n < card_limit:

    cardnum = random.randrange(4000000000000000, 6000000000000000, 1)
    if is_cardnumber(str(cardnum)) and is_luhn_valid(cardnum) :
        if rows == 0:
            print("INSERT INTO CARDDATA (", end = '')

        print(cardnum, end='')
        n = n + 1
        rows = rows + 1
        if rows == 5:
            print("", end = '')
        else:
            print("", end = ', ')
    if rows == 5 and n < card_limit:
        print(');')
        rows = 0
    if n == card_limit:
        print(");")
        
        


