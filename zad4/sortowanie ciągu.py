# -*- coding: utf-8 -*-
"""
Created on Sat May 15 08:06:45 2021

@author: colib
"""

print ('Hello Word')

'sortowanie liczb ciągu'

x=[4,5,2,9,8,5,6]
n=7
i = 0
j = i +1


for i in range (0, n-1):
    
    for j in range (i+1,n):
        if x[i] > x[j]:
            z=x[i]
            x[i] = x[j]
            x[j]=z
        
print ('wynik sortowania ciągu, to:', x)
