# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 15:38:05 2023

@author: Amar Doshi
"""

text = '''
It was a dark and stormy night; the rain fell in torrents—except at occasional
intervals, when it was checked by a violent gust of wind which swept up the streets
(for it is in London that our scene lies), rattling along the housetops, and fiercely
agitating the scanty flame of the lamps that struggled against the darkness.
'''

# - Edward Bulwer-Lytton's 1830 novel Paul Clifford


total = 0
vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for C in text:
    c = C.lower()

    if c in vowels:
        vowels[c] += 1
        total += 1

print()

for k, v in vowels.items():
    print(f'{k}: {v: >3}')

print()
print(f'Total Vowels: {total}')
