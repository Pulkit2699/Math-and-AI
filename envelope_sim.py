# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:29:53 2020

@author: pulki
"""
import random
def pick_envelope(switch, verbose):
    #Randomly distribute the three black/one red balls into two envelopes 
    set1 = ['b','b','b','r']
    Envelope0 = random.sample(set1,2)
    if(verbose == True):
        print("Envelope 0:", end = " ")
    for i in range (len(Envelope0)):
        if(verbose == True):
            print(Envelope0[i], end = " ")
    Envelope1 = set1.copy()
    Envelope1.remove(Envelope0[0])
    Envelope1.remove(Envelope0[1])
    if(verbose == True):
        print()
        print("Envelope 1:", end = " ")
        for i in range (len(Envelope1)):
            print(Envelope1[i], end = " ")
        print()
    #Randomly select one envelope
    
    index = random.randint(0,1)
    if(verbose == True):
        if(index == 0):
            print("I picked envelope 0")
        elif(index == 1):
            print("I picked envelope 1")
    
    #Randomly select a ball from the envelope
    ballIndex = random.randint(0,1)
    if(index == 0):
        chosen = Envelope0[ballIndex]
        if(verbose == True):
            print("and drew a ", chosen)
    elif(index == 1):
        chosen = Envelope1[ballIndex]
        if(verbose == True):
            print("and drew a ", chosen)
    if(chosen == 'r'):
        return True
    
    if(switch):
        if(index == 1):
            index = 0
            if(verbose == True):
                print("Switch to envelope 0")
        elif(index == 0):
            index = 1
            if(verbose == True):
                print("Switch to envelope 1")
            
    if(index == 0):
        if 'r' in Envelope0:
            return True
        else:
            return False
    elif(index == 1):
        if 'r' in Envelope1:
            return True
        else:
            return False
        
def run_simulation(n):
    print("After",n, "simulations:")
    trueCounter = 0
    for i in range(n):
        check = pick_envelope(True, False)
        if(check):
            trueCounter = trueCounter + 1
    print("Switch successful:", trueCounter/n * 100,"%")
    trueCounter = 0
    for i in range(n):
        check = pick_envelope(False, False)
        if(check):
            trueCounter = trueCounter + 1
    print("No-switch successful:", trueCounter/n * 100,"%")
    
        
    
    