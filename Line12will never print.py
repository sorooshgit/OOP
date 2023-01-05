# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:34:48 2022

@author: SOROUSH
"""
x=int(input('Enter a number:'))
if x < 2 :
    print('Below 2')
elif x < 20 :
    print('Below 20')
elif x < 10 : 
    print('Below 10')
else :
    print('Something else')
print('Line 12 will never print regardless of the value for x')
