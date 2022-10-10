# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 19:56:40 2022

@author: muzi
"""

from math import floor,ceil

def find(m):
    a = 180.105
    b = 95.988
    c = 18.01
    
    high = ceil(m/b)
    
    p = []
    for x in range(high):
        for y in range(high):
            for h in range(x+y-1,x+y+3):
                if m-1 < a*x+b*y-c*h < m+1:
                    p.append((x,y,h,a*x+b*y-c*h))
    return p
