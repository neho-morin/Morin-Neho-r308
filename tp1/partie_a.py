### Création du dictionnaire avec les trois étudiants
d = {"Alice": 12, "Bob": 15, "Claire": 9.5}

### Création de la fonction ajouter un etudiant
def ajouter_etudiant(d, nom, note):
    d[nom] = note

### Création de la fonction moyenne classe
def moyenne_classe(d):
    if d != {}:
        nombre = len(d)
        somme = sum(d.values())
        moyenne = somme / nombre
        return moyenne
    else:
        return "Rien"

### Création de la fonction qui renvoie le meilleur étudiant
def meilleur_etudiant(d):
    if d != {}:
        best = max(d, key=d.get)
        note = d.get(best)
        return (best, note)
    else:
        return "Personne", "Rien"

### Création de la fonction de sauvegarde et la gestion des erreurs
def sauvegarder(d, chemin):
    try:
        with open(chemin, "w", encoding="utf-8") as f:
            for nom, note in d.items():
                f.write(f"{nom}:{float(note)}\n")
    except OSError as e:
        print(f"Erreur code {e}")

### Création de la fonction qui va recherger
def charger(chemin):
    d = {}
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            for ligne in f:
                try:
                    ligne = ligne.strip()
                    nom, note = ligne.split(":")
                    d[nom] = float(note.strip())
                except ValueError as e:
                    print(f"Erreur de format dans la ligne '{ligne}', code {e}")
    except OSError as e:
        print(f"Erreur, fichier absent ou inaccessible, code {e}")
    return d

### Corps du jeu
if __name__ == "__main__":
    print("Dictionnaire initial:", d)
    ajouter_etudiant(d, "David", 14)
    print("Dictionnaire après ajout de David:", d)
    print("Moyenne de la classe:", moyenne_classe(d))
    meilleur = meilleur_etudiant(d)
    print(f"Meilleur étudiant: {meilleur[0]} avec une note de {meilleur[1]}")
    chemin_fichier = "etudiants.txt"
    sauvegarder(d, chemin_fichier)
    d_chargé = charger(chemin_fichier)
    print("Dictionnaire chargé depuis le fichier:", d_chargé)