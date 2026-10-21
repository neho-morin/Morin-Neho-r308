###MANIPULATION DE MOT###
### Iportation du module random ###
import random

###Ouverture du fichier###
def charger(chemin):
    d = {}
    i = 0
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            for ligne in f:
                try:
                    ligne = ligne.strip()
                    d[i] = ligne
                    i =+ 1
                except ValueError as e:
                    print(f"Erreur de format dans la ligne '{ligne}', code {e}")
    except OSError as e:
        print(f"Erreur, fichier absent ou inaccessible, code {e}")
    return d

### Choix du mot ###
def choisir_mot(list):
    mot = {}
    mot = random.choice(list)
    return mot

### Création et affichage du masque ###
def masque(mot):
    nombre = len(mot)
    chaine_spe = ["_"] * nombre
    print(f"Le masque est : {chaine_spe}")

### Corps du programme ###
print("Ouverture du fichier")
chemin_du_fichier = "liste_de_mot.txt"
liste = charger(chemin_du_fichier)
print("Choix du mot")
mot = choisir_mot(liste)
print("Affichage du mot choisie")
print(f"Le mot est : {mot}")
nombre = len(mot)
print(f"Ce mot à {nombre} lettre")
print("Affichage du masque")
masque(mot)