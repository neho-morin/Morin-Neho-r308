### Le programme principale ###

class Livre:
    def __init__(self, titre, auteur, annee, disponible=True, emprunteur=None):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = disponible
        self.emprunteur = emprunteur      # nom de l'emprunteur, ou None

    def afficher(self):
        if self.disponible:
            etat = "disponible"
        else:
            etat = f"emprunté par {self.emprunteur}"
        print(f"{self.titre} - {self.auteur} ({self.annee}) : {etat}")

    def emprunter(self, nom):
        if not self.disponible:
            return False
        self.disponible = False
        self.emprunteur = nom
        return True

    def rendre(self):
        if self.disponible:
            return False
        self.disponible = True
        self.emprunteur = None
        return True


class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.emprunts = []                # liste de Livre

    def emprunter_livre(self, livre):
        if livre.emprunter(self.nom):
            self.emprunts.append(livre)
            return True
        return False

    def rendre_livre(self, livre):
        if livre in self.emprunts and livre.rendre():
            self.emprunts.remove(livre)
            return True
        return False

    def afficher_emprunts(self):
        if not self.emprunts:
            print(f"{self.nom} n'a aucun emprunt.")
        for livre in self.emprunts:
            livre.afficher()

### Test ###
l = Livre("1984", "Orwell", 1949)
print(l.emprunter("Ana"))   # True
print(l.emprunter("Léo"))   # False
print(l.rendre())           # True