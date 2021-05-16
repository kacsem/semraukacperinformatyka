# -*- coding: utf-8 -*-
"""
Created on Sun May 16 15:19:28 2021

@author: colib
"""

def dodawanie (x,y,z):
    suma = x+y+z
    return suma 

x= input("podaj pierwszą zmienną i wcisnij enter: ")
x=float(x)
y= input("podaj drugą zmienną i wcisnij enter: ")
y=float(y)
z= input("podaj trzecią zmienną i wcisnij enter: ")
z=float(z)



print ('suma twoich liczb, to:', dodawanie(x, y, z))