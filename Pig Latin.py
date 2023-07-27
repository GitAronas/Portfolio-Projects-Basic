# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 18:11:36 2023

@author: Amar Doshi
"""

text = '''It was a dark and stormy night ; the rain fell in torrents—except at occasional intervals , when it was checked by a violent gust of wind which swept up the streets ( for it is in London that our scene lies ) , rattling along the housetops , and fiercely agitating the scanty flame of the lamps that struggled against the darkness .'''

# - Edward Bulwer-Lytton's 1830 novel Paul Clifford

PUNCS = '();,.'
VOWELS = ('a', 'e', 'i', 'o', 'u')

def PigLatin(word):
    if word[0] in VOWELS:
        return word + 'way'
    elif word in PUNCS:
        return word
    else:
        return word[1:] + word[0] + 'ay'


words = text.split(' ')

pl = []

for word in words:
    pl.append(PigLatin(word))

translated = ' '.join(pl)

print()
print(text)
print()
print(translated)
