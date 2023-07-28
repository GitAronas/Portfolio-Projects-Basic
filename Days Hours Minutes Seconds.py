# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 15:27:25 2023

@author: Amar Doshi
"""


def getDaysHoursMinutesSeconds(totalSeconds):
    if totalSeconds == 0:
        return '0s'

    t = []

    d, h = divmod(totalSeconds, 86400)
    if d > 0:
        t.append(str(d) + 'd')

    h, m = divmod(h, 3600)
    if h > 0:
        t.append(str(h) + 'h')

    m, s = divmod(m, 60)
    if m > 0:
        t.append(str(m) + 'm')

    if s > 0:
        t.append(str(s) + 's')

    return ' '.join(t)

