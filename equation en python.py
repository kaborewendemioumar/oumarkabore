# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 12:48:00 2025

@author: THINKPAD T560
"""

import math
a=float(input("donner a"))
b=float(input("donner b"))
c=float(input("donner c"))
d=b**2-4*a*c
if(d==0):
    x0=-b/(2*a)
    print("la solution double est:",x0)
else:
    if(d>0):
        x1=(-b-math.sqrt(d))/(2*a)
        x2=(-b+math.sqrt(d))/(2*a)
        print("les solutions sont:",x1,x2)
    else:
        print("pas de solution")