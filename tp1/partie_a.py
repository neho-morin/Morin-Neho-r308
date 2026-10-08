### Création du dictionnaire avec les trois étudiants
d = {"Alice": 12, "Bob": 15, "Claire": 9.5}

### Création de la fonction ajouter un etudiant
def ajouter_etudiant(d, nom, note):
    d[nom] = note
    return

### Création de la fonction moyenne classe
def moyenne_classe(d):
    nombre = len(d)
    somme = sum(d.values())
    moyenne = somme / nombre
    return moyenne

### Création de la fonction qui renvoie le meilleur étudiant
def meilleur_etudiant(d):
    best = max(d, key=int)
    note = d.get("best")
    return best & note
