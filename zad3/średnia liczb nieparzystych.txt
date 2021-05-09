# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:34:35 2021

@author: colib
"""

print ('hello')

a =3
b =7

suma=0
i=1
j=0
srednia=1

print (a,b)

if a%2!=0:
    a= a+1

for i in range (a,b+1,2):
    suma=suma+i
    j= j+1

srednia = suma / j 
print ('Średnia arytmetyczna liczb nieparzystyh z przedziału <a,b> =', srednia)