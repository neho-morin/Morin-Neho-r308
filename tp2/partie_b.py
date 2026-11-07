### Jeu de classe joueur ###
### Importation du module random ###
import random

### Manipulation du joueur ###
class JoueurHumain:
    def prochain_coup(self, tab, symbole):
        while True:
            try:
                x = int(input("Ligne (0-2) : "))
                y = int(input("Colonne (0-2) : "))
                return (x, y)
            except ValueError:
                print("Entre un nombre entier.")

class JoueurIA:
    def prochain_coup(self, tab, symbole):
        libres = [(x, y) for x in range(3) for y in range(3)
                  if tab.cases[x][y] == " "]
        return random.choice(libres)