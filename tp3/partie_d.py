from partie_b import Livre, Utilisateur, Bibliotheque

FICHIER = "biblio.csv"

def main():
    b = Bibliotheque()
    b.charger(FICHIER)
    while True:
        print("\n1 Ajouter un livre | 2 Ajouter un utilisateur | 3 Emprunter")
        print("4 Rendre | 5 Afficher les livres | 6 Quitter et sauvegarder")
        choix = input("Choix : ").strip()
        if choix == "1":
            titre = input("Titre : ").strip()
            auteur = input("Auteur : ").strip()
            try:
                annee = int(input("Année : "))
            except ValueError:
                print("L'année doit être un nombre.")
                continue
            b.ajouter_livre(Livre(titre, auteur, annee))
        elif choix == "2":
            b.ajouter_utilisateur(Utilisateur(input("Nom : ").strip()))
        elif choix == "3":
            ok = b.emprunter(input("Nom : ").strip(), input("Titre : ").strip())
            print("Emprunt réussi" if ok else "Échec de l'emprunt")
        elif choix == "4":
            ok = b.rendre(input("Nom : ").strip(), input("Titre : ").strip())
            print("Livre rendu" if ok else "Échec du retour")
        elif choix == "5":
            b.afficher_livres()
        elif choix == "6":
            b.sauvegarder(FICHIER)
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()