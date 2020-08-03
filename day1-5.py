# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:28:35 2020

@author: user
"""
taste=input("成績:")
taste=int(taste)
if taste>0 and taste<100:
    if taste>=90:
        print("a等級")
    elif taste>=80:
        print("b等級")
    elif taste>=70:
        print ("C等級")
    elif taste>=60:
        print ("d等級")
    else:
        print ("你好弱")
else:   
    print("請輸入1~100")        