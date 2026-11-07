### Importation des modules nécessaires ###
from partie_b import Bibliotheque
from partie_a import Livre, Utilisateur

### Programme Principale ###
def sauvegarder(self, chemin):
        try:
            with open(chemin, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                for l in self.livres.values():
                    w.writerow([l.titre, l.auteur, l.annee,
                                l.disponible, l.emprunteur or ""])
            return True
        except OSError as e:
            print(f"Erreur de sauvegarde : {e}")
            return False

def charger(self, chemin):
    try:
        with open(chemin, "r", newline="", encoding="utf-8") as f:
            for ligne in csv.reader(f):
                if len(ligne) != 5:
                    continue
                titre, auteur, annee, dispo, emprunteur = ligne
                try:
                    annee = int(annee)
                except ValueError:
                    continue
                livre = Livre(titre, auteur, annee,
                                dispo == "True", emprunteur or None)
                self.ajouter_livre(livre)
                if emprunteur:
                    if emprunteur not in self.utilisateurs:
                        self.ajouter_utilisateur(Utilisateur(emprunteur))
                    self.utilisateurs[emprunteur].emprunts.append(livre)
    except OSError:
        print("Aucun fichier de sauvegarde : départ à vide.")

### Test du programme ###
b = Bibliotheque()
b.ajouter_livre(Livre("1984", "Orwell", 1949))
b.ajouter_utilisateur(Utilisateur("Ana"))
b.emprunter("Ana", "1984")
b.sauvegarder("biblio.csv")

b2 = Bibliotheque()
b2.charger("biblio.csv")
b2.afficher_livres()                  # 1984 emprunté par Ana
print(b2.rendre("Ana", "1984"))       # True