#!/usr/bin/python

import sys
import CardNumberGenerator as cgn
import LuhnVerification as luhn


card_limit = int(sys.argv[1])
n = 0
rows = 0
table = str(sys.argv[2])

print("CREATE TABLE", table, "(a varchar(50), b varchar(50), c varchar(50), d varchar(50), e varchar(50));")


while n < card_limit:

    cardnum = cgn.card_num_gen()
    if cgn.is_cardnumber(str(cardnum)) and luhn.is_luhn_valid(cardnum) :
        if rows == 0:
            print("INSERT INTO", table, "VALUES (", end = "")
        
        print("'", end = '')
        print(cardnum, end="'")
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
        
        


