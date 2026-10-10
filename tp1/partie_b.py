### Création d'un jeu de choix
### Importation de la bibliothêque random
import random

### Cration de la fonction du jeu
def jeu(n):
    p = 0
    essais = 0
    while essais < 10:
        print(f"Tu as {10 - essais} essais")
        repnse = input("Choisis un nombre ? ")
        if repnse.isdigit() == False:
            print("Erreur, tu dois entrer un nombre")
        else:
            essais += 1
            reponse = int(repnse)
            if 1 <= reponse <= 100:
                if reponse < n:
                    print("C'est plus")
                elif reponse > n:
                    print("C'est moins")
                else:
                    print("Bravo, tu as trouvé le nombre")
                    p = 1
                    break
            else:
                print("Tu na pas respecter la règle du jeu -1 esseai")
        if p == 0 and essais == 10:
            print("Tu as perdu, le nombre était", n)
        
 
### Corps du jeu
### On done les instructions du jeu
print("Voici dans un jeu de devinette")
print("VOICI LES RÉGLE DU JEU :")
print("Je vais choisir un nombre entre 1 et 100, toit tu devra le trouver")
print("Tu devra donner un nombre entre 1 et 100")
print("Tu as 10 essais pour trouver le nombre")
print("Si tu ne trouve pas le nombre, tu perdra le jeu")
print("Si tu trouve le nombre, tu gagne le jeu")
print("Si tu ne respecte pas les règles du jeu, tu perdra un essai\n")
print("BONNE CHANCE !\n")

i = 0
while i == 0:
    ### On initialise le nombre aléatoire
    n = random.randint(1, 100)
    ### On démarre le jeu
    jeu(n)
    ### On demande si le joueur veut rejouer
    i = input("Veux tu rejouer ? (oui/non : Pas de Majuscules) ")
    if i == "non":
        print("Merci d'avoir jouer, à la prochaine")
        i = 1
    elif i == "oui":
        i = 0
    else:
        print("Erreur, tu dois répondre par oui ou non (Fin de la partie)")
        i = 1

print("Fin du jeu")