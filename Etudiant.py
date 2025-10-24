# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 23:33:59 2025

@author: THINKPAD T560
"""

#Etudiant.py
import numpy as np
class Etudiant:
    def __init__(self,matricule,nom,prenom,nbrNotes):
        self.matricule=matricule
        self.nom=nom
        self.prenom=prenom
        self.nbrNotes=nbrNotes
        self.tabNote=[]
    def get_matricule(self):
        return self.matricule
    def get_nom(self):
        return self.nom
    def get_prenom(self):
        return self.prenom
    def get_nbrNotes(self):
        return self.nbrNotes
    def get_tabNotes(self):
        return self.tabNotes
    def set_matricule(self,matricule):
        self.matricule=matricule
    def set_nom(self,nom):
        self.nom=nom
    def set_prenom(self,prenom):
        self.prenom=prenom
    def set_nbrNotes(self,nbrNotes):
        self.nbrNotes=nbrNotes
    def saisie(self):
        for i in range(self.nbrNotes):
            note=float(input(f"entrer la note{i+1}:"))
            self.tabNotes.append(note)
    def afficher(self):
        print(f"Matricule:{self.matricule},Nom:{self.nom},prenom:{self.prenom}")
        print(f"Notes:{self.tabNotes}")
        print(f"Moyenne:{self.moyenne()}")
        print("Admis" if self.admis() else "Ajourne")
    def moyenne (self):
        return sum(self.tabNotes)/ len(self.tabNotes)
    def admis(self):
        return( sum(self.tabNotes)/ len(self.tabNotes))>=10 
        
        