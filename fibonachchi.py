# -*- coding: utf-8 -*-
"""
Created on Mon May  8 19:22:11 2023

@author: pk
"""

def fibonachchi (numb) :
    numbers = []
    for x in range(numb) :
        
        if x == 0 or x == 1:
            numbers.append(1)
        
        else:
            numbers.append(numbers[-1] + numbers[-2])
        
    
    return numbers

numb1 = fibonachchi(24)

print(numb1)


