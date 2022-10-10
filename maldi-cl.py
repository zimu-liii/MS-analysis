# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 13:09:49 2022

@author: muzi
"""

from math import floor,ceil

def find_cl(m):
    a = 180.105
    b = 95.988
    c = 18.01
    d = 34.97
    
    high = ceil(m/b)
    
    p = []
    for x in range(high):
        for y in range(high):
            for h in range(x+y,(3*x+4*y)//2):
                if m-3 < (a+d)*x+b*y-c*h < m+3:
                    p.append((x,y,h,(a+d)*x+b*y-c*h))
    return p

def find_clless(m):
    a = 180.105
    b = 95.988
    c = 18.01
    d = 34.97
    
    high = ceil(m/b)
    
    p = []
    for x in range(high):
        for y in range(high):
            for h in range(x+y,(3*x+4*y)//2):
                if m-3 < a*x+b*y-c*h+d*(x-1) < m+3:
                    p.append((x,y,h,a*x+b*y-c*h+d*(x-1)))
    
    return p
