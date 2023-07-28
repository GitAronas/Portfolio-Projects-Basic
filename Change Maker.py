# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 18:13:26 2023

@author: Amar Doshi
"""


def makeChange(amount: int):
    '''
    Amount in cents.
    '''

    dic = {}
    coins = {25: 'quarters', 10: 'dimes', 5: 'nickels', 1: 'pennies'}

    for coin, name in coins.items():
        d, r = divmod(amount, coin)

        if d > 0:
            dic[name] = d
            amount = r

        if amount == 0: break

    return dic

