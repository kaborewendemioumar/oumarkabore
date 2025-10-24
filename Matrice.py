# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 17:35:53 2025

@author: THINKPAD T560
"""

#Matrice.py
import numpy as np
class Matrice:
    def __init__(self, A, b):
        self.A=np.array(A,dtype=float)
        self.b=np.array(b,dtype=float)
    def affiche(self):
        print("Matrice A=\n",self.A)
        print("Matrice b=",self.b)
    def resoudre(self):
            x=np.linalg.solve(self.A, self.b)
            return x