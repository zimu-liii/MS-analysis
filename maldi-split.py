# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 10:00:40 2022

@author: muzi
"""

from math import floor,ceil

def find_split_cl(m):
    a = 180.105
    b = 95.988
    
    a2 = a-9*2
    a3 = a-9*3
    
    b2 = b-9*2
    b3 = b-9*3
    b4 = b-9*4
    
    d = 34.97
    
    higha = ceil(m/a)
    highb = ceil(m/b)
    
    p = []
    for x2 in range(higha):
        for x3 in range(higha):
            for y3 in range(highb):
                for y2 in range(highb):
                    for y4 in range(highb):
                        if (x2*2+x3*3+y2*2+y3*3+y4*4)%2 == 0:
                            m0 = a2*x2+a3*x3+d*(x2+x3)+b2*y2+b3*y3+b4*y4
                            if m-3 < m0 < m+3:
                                p.append((x2,x3,y2,y3,y4,m0))
    return p
