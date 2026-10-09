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
    except OSError:
        print("Erreur lors de l'ouverture du fichier, donner un nom correcte")

### Création de la fonction qui va recherger
def charger(chemin):
    d = {}
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            for ligne in f:
                