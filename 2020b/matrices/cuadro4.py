#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 07:13:46 2020

@author: daniel
"""

import numpy as np

a = np.zeros((4,4))
b = np.zeros((4,4))
c = np.zeros((4,4))

ren = 0
col = 0
col2 = 3

for i in range(1,17) :
    if (ren == col) | (ren == col2) :
        a[ren,col] = i
    
    col = col + 1
    col2 = col2 - 1
    if i % 4 == 0 :
        ren = ren + 1
        col = 0
        col2 = 3
        
        
for ren in range(4) :
    for col in range(4) :
        print("%4d"%a[ren][col], end='')
    print()

ren = 3
col = 0
col2 = 3

for i in range(1,17) :
    if ((ren != col) & (ren != col2)) :
        b[ren,col2] = i
    
    col = col + 1
    col2 = col2 - 1
    if i % 4 == 0 :
        ren = ren - 1
        col = 0
        col2 = 3
        
print()
for ren in range(4) :
    for col in range(4) :
        print("%4d"%b[ren][col], end='')
    print()
    
    
c = a + b
print()
for ren in range(4) :
    for col in range(4) :
        print("%4d"%c[ren][col], end='')
    print()
