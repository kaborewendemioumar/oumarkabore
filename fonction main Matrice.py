# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 17:48:37 2025

@author: THINKPAD T560
"""

#main.py
from Matrice import Matrice
def main():
    A=[[2,1],[1,3]]
    b=[8,13]
    mat=Matrice(A,b)
    mat.affiche()
    solution= mat.resoudre()
    print("solution du systeme x=",solution)