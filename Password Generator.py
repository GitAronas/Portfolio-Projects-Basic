# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:29:43 2023

@author: Amar Doshi
"""

from random import choice, shuffle

NUMBERS = '0123456789'
SPECIAL = '~!@#$%^&*()_+'
UPPER_LETTERS = 'ABCDEFGHIJKLMONPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmonpqrstuvwxyz'

ALL = NUMBERS + SPECIAL + UPPER_LETTERS + LOWER_LETTERS

def generatePassword(length=12):
    if length < 12:
        length = 12

    pw = []

    pw.append(choice(UPPER_LETTERS))
    pw.append(choice(LOWER_LETTERS))
    pw.append(choice(NUMBERS))
    pw.append(choice(SPECIAL))

    shuffle(pw)

    for _ in range(4, length):
        pw.append(choice(ALL))

    return ''.join(pw)
