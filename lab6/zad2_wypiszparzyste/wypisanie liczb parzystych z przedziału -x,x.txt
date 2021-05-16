# -*- coding: utf-8 -*-
"""
Created on Sun May 16 13:47:01 2021

@author: colib
"""

print ('Hello')

x= input ("wpisz liczbę całkowitą X i nacisnij enter:")

x=int(x)

z= -1*x 

for i in range (z,x+1,1):
   if i%2==0:
       print (i)