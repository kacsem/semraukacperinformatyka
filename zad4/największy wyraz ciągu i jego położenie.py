# -*- coding: utf-8 -*-
"""
Created on Sat May 15 00:31:31 2021

@author: colib
"""

'wypisywanie największego wyrazu coagu i jesgo położenia'

x= [4,5,15,4,89,2,1,5,2,1,5,2,45,1,5,15,145]
n=17

max=x[0]
imax=0
i=1

print ('wyrazy ciągu, to:', x)
print ('liczebnosć ciągu, to;', n)

for i in range (1,n):
    if x[i]>max:
        max = x[i]
        imax = i 
        
print(' wartosć największa ciągu, to:', max)
print(' ,a jej położenie, to:', imax)
