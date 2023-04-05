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
    
    count=1
    num=n*n
    
    i=n//2
    j=n-1
    
    while(count<=num):
        if(i<0 and j==n):
            i=0
            j=n-2
        else:
            if(i<0):
                i=n-1
            if(j==n):
                j=0
        if(key[i][j]!=0):
            i=i+1
            j=j-2
        else:
            key[i][j]=count
            count+=1
            i=i-1
            j=j+1
            
    print("Your key is")
    for i in range(n):
        for j in range(n):
            print(key[i][j], end=" ")
        print()
