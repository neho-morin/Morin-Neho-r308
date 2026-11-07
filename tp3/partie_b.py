### Pour le fonctionnement de la partie C ###
from partie_a import Livre, Utilisateur

class Bibliotheque:
    def __init__(self):
        self.livres = {}            # titre -> Livre
        self.utilisateurs = {}      # nom -> Utilisateur

    def ajouter_livre(self, livre):
        self.livres[livre.titre] = livre

    def ajouter_utilisateur(self, utilisateur):
        self.utilisateurs[utilisateur.nom] = utilisateur

    def emprunter(self, nom, titre):
        if nom not in self.utilisateurs or titre not in self.livres:
            return False
        return self.utilisateurs[nom].emprunter_livre(self.livres[titre])

    def rendre(self, nom, titre):
        if nom not in self.utilisateurs or titre not in self.livres:
            return False
        return self.utilisateurs[nom].rendre_livre(self.livres[titre])

    def afficher_livres(self):
        print("--- Disponibles ---")
        for livre in self.livres.values():
            if livre.disponible:
                livre.afficher()
        print("--- Empruntés ---")
        for livre in self.livres.values():
            if not livre.disponible:
                livre.afficher()