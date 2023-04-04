# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 06:21:37 2023

@author: Thiruvarulselvan K
"""

def sudoku_key(n):
    key=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        key.append(l)

    for i in range(n):
        for j in range(n):
            print(key[i][j], end=" ")
        print()
