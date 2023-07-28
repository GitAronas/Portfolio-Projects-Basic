# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:35:14 2023

@author: Amar Doshi
"""

# rock beats scissors, paper beats rock, and scissors beats paper.

'''
r > s
p > r
s > p
'''

def rpsWinner(player1, player2):
    R = 'rock'
    P = 'paper'
    S = 'scissors'

    wins = ((R, S), (P, R), (S, P))

    if player1 == player2:
        return 'tie'
    elif (player1, player2) in wins:
        return 'player one'
    elif (player2, player1) in wins:
        return 'player two'
    else:
        return 'Error: Invalid value(s)!'

