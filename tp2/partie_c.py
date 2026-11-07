### On importe de la partie A la grille ###
from partie_a import Grille

def partie(joueur_x, joueur_o, verbose=True):
    g = Grille()
    joueurs = [(joueur_x, "X"), (joueur_o, "O")]
    tour = 0
    while True:
        joueur, symbole = joueurs[tour % 2]
        if verbose:
            g.afficher()
        x, y = joueur.prochain_coup(g, symbole)
        if not g.jouer(x, y, symbole):
            continue                    # coup invalide : le même joueur rejoue
        if g.est_gagnant(symbole):
            if verbose:
                g.afficher()
                print(f"{symbole} gagne !")
            return symbole
        if g.est_plein():
            if verbose:
                g.afficher()
                print("Match nul")
            return None
        tour += 1

if __name__ == "__main__":
    partie(JoueurHumain(), JoueurIA())