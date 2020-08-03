# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:06:19 2020

@author: user
"""
En=input("英文成績:")
Ma=input("數學成績:")
En=int(En)
Ma=int(Ma)
if En>90 and Ma>90:
    print ("獎品iphone11一台!")
elif En>60 or Ma>60:
    print ("再加油")   
else:
    print ("去拿棍子!")    
