### Jeu de morpion ###
### Importation du module random ###
import random

### Manipulation du plateau ###
class grille:
    def __init__(self):
        self.plateau = [["T", "T", "T"], ["T", "T", "T"], ["T", "T", "T"]]

    #def tir(self, Ligne, Collone, Pion):
        #self.plateau[Ligne][Collone] = Pion

    def afficher(self):
        value = 0
        for i in self.plateau:
            val = "|"
            t = 0
            for x in i:
                print(x, end=' ')
                if t < 2:
                    print(val, end=(' '))
                value += 1
                t += 1

            if value == 3:
                print("")
                value = 0

            
           
            
### Structure principale du jeu ###
j = grille()
j.afficher()
#PionJ = "X"
#PionO = "O"
#print("Jeu d'essai")

#print("Joueur choisie ton tir : ")
#Ligne = int(input("Choisie une ligne (1 - 3)")) - 1
#Collone = int(input("Choisie la collone (1 - 3)")) - 1
#j.tir(Ligne, Collone, PionJ)