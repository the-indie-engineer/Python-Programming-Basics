# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 06:39:51 2023

@author: Star
"""

with open("flight_log.txt","r+") as myfile:
    myfile.write("Logging initialized")
myfile.close()