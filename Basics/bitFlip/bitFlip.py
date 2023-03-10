# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 06:57:03 2023

@author: Star
"""

import random

def bitFlip(x):
    ind = random.randint(0,len(x)-1)
    p= random.randint(0,2)
    if(p==1):
        if(x[ind]=='0'):
            x[ind]='1'


with open("flight_log.txt","r+") as myfile:
    x=myfile.read()
    x=list(x)
for i in range(0,100):
    bitFlip(x)
print(x)
with open("flight_log.txt","r+") as myfile:
    x=str(x)
    myfile.write(x)
    myfile.close()