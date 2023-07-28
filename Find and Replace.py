# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 14:30:30 2022

@author: Amar Doshi
"""

def findAndReplace(text, oldText, newText):
    s1, s2, s3 = text.partition(oldText)

    if s1 == text:
        return s1
    else:
        return s1 + newText + findAndReplace(s3, oldText, newText)

