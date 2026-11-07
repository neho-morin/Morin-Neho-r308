from partie_b import JoueurHumain, JoueurIA
from partie_bonus import JoueurIAMalin
from partie_c import partie

JOUEURS = {
    "1": ("Humain", JoueurHumain),
    "2": ("IA aléatoire", JoueurIA),
    "3": ("IA maligne", JoueurIAMalin),
}

def choisir(symbole):
    print(f"Joueur {symbole} :")
    for cle, (nom, _) in JOUEURS.items():
        print(f"  {cle} - {nom}")
    while True:
        rep = input("Ton choix : ").strip()
        if rep in JOUEURS:
            return JOUEURS[rep][1]()      # on crée l'objet
        print("Choix invalide.")

def main():
    scores = {"X": 0, "O": 0, "Nul": 0}
    joueur_x = choisir("X")
    joueur_o = choisir("O")
    while True:
        gagnant = partie(joueur_x, joueur_o)
        scores[gagnant or "Nul"] += 1
        print("Scores :", scores)
        if input("Rejouer ? (o/n) ").strip().lower() != "o":
            break

if __name__ == "__main__":
    main()