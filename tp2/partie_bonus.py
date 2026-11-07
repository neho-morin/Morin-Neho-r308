### On importe le jeur IA de la partie B ###
from partie_b import JoueurIA

class JoueurIAMalin:
    def _coup_gagnant(self, tab, symbole):
        for x in range(3):
            for y in range(3):
                if tab.cases[x][y] == " ":
                    tab.cases[x][y] = symbole       # on essaie
                    gagne = tab.est_gagnant(symbole)
                    tab.cases[x][y] = " "           # on annule
                    if gagne:
                        return (x, y)
        return None

    def prochain_coup(self, tab, symbole):
        adversaire = "O" if symbole == "X" else "X"
        coup = self._coup_gagnant(tab, symbole)         # 1. gagner
        if coup is None:
            coup = self._coup_gagnant(tab, adversaire)  # 2. bloquer
        if coup is None:
            return JoueurIA().prochain_coup(tab, symbole)  # 3. hasard
        return coup