# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 06:02:19 2023

@author: Thiruvarulselvan K
"""

import random

rockets=['SN1', 'PSLV', 'GSLV', 'Falcon 9', 'Saturn V', 'Rohini', 'Starliner']


def create_qn(pick):
    n=len(pick)
    letters=list[pick]
    temp=[]
    for i in range(n):
        if letters==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return qn

def is_present(letter,pick):
    c=pick.count(letter)
    if c==0:
        return False
    else:
        return True
    
def unlock(qn,pick,letter):
    ref=list(pick)
    n=len(pick)
    temp=[]
    qn_list=list(qn)
    for i in range(n):
        if ref[i]==' ' or ref[i]==letter: temp.append(ref[i])
        else:
            if qn_list[i]=='*': temp.append('*')
            else: temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new

def play():
    p1name=input("Player 1 please entern your name!")
    p2name=input("Player 2 please enter your name!")
    pp1=0
    pp2=0
    
    turn=0
    will=True
    
    while(will):
        if turn%2==0:
            print(p1name,", your turn now!")
            pick=random.choice(rockets)
            qn=create_qn(pick)
            print(qn)
            
            modified_qn=qn
            not_said=True
            
            while(not_said):
                letter=input("Your letter: ")
                
                if(is_present(letter,pick)):
                    modified_qn=unlock(modified_qn,pick,letter)
                    print(modified_qn)
                    
                    d=input("1 to guess \n 2 to reveal a letter")
                    if d==1:
                        ans=input("Enter the rocket name!")
                        if ans==pick:
                            pp1=pp1+1
                            print("Correct")
                            print(p1name,", your score is", pp1)
                            
                            not_said=False
                        else:
                            print("Wrong answer dude")
                else:
                    print(" Not found")
                    
                c=input("1 to continue \n 0 to quit\n")
                if c==0:
                    print(p1name, ", your score is",pp1)
                    print(p2name, ", your score is",pp2)
                    print("Thanks for playing\n Have a nice day")
                    willing=False
        else:
            print(p2name,", your turn now!")
            pick=random.choice(rockets)
            qn=create_qn(pick)
            print (qn)
            
            modified_qn=qn
            not_said=True
            
            while(not_said):
                letter=input("Your letter: ")
                
                if(is_present(letter,pick)):
                    modified_qn=unlock(modified_qn,pick,letter)
                    print(modified_qn)
                    
                    d=input("1 to guess \n 2 to reveal a letter")
                    if d==1:
                        ans=input("Enter the rocket name!")
                        if ans==pick:
                            pp2=pp2+1
                            print("Correct")
                            print(p2name,", your score is", pp2)
                            
                            not_said=False
                        else:
                            print("Wrong answer dude")
                else:
                    print(" Not found")
                    
                c=input("1 to continue \n 0 to quit")
                if c==0:
                    print(p1name, ", your score is",pp1)
                    print(p2name, ", your score is",pp2)
                    print("Thanks for playing\n Have a nice day")
                    will=False

        turn=turn+1
    
play()