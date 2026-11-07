### Jeu de morpion ###
### Manipulation du plateau ###
class Grille:
    def __init__(self):
        # x = ligne, y = colonne (d'après le jeu d'essai du sujet)
        self.cases = [[" " for _ in range(3)] for _ in range(3)]

    def afficher(self):
        lignes = [" | ".join(ligne) for ligne in self.cases]
        print("\n---------\n".join(lignes))

    def jouer(self, x, y, joueur):
        if not (0 <= x < 3 and 0 <= y < 3):
            print("Hors grille")
            return False
        if self.cases[x][y] != " ":
            print("Case occupée")
            return False
        self.cases[x][y] = joueur
        return True

    def est_gagnant(self, j):
        c = self.cases
        for i in range(3):
            if all(c[i][k] == j for k in range(3)):      # ligne i
                return True
            if all(c[k][i] == j for k in range(3)):      # colonne i
                return True
        if all(c[k][k] == j for k in range(3)):          # diagonale \
            return True
        if all(c[k][2 - k] == j for k in range(3)):      # diagonale /
            return True
        return False

    def est_plein(self):
        return all(case != " " for ligne in self.cases for case in ligne)

            
           
            
### Structure principale du jeu ### --> TEST
#g = Grille()
#g.jouer(0, 0, "X"); g.jouer(0, 1, "O"); g.jouer(1, 1, "X")
#g.afficher()
#g.jouer(0, 0, "O")        # refusé : occupée
#g.jouer(3, 0, "O")        # refusé : hors grille
#print(g.est_gagnant("X")) # False
#g.jouer(2, 2, "X")
#print(g.est_gagnant("X")) # True
