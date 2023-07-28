# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 16:47:42 2023

@author: Amar Doshi
"""

def isLeapYear(year):
    return (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0)
