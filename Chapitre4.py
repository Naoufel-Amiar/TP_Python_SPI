import math
from turtle import *
from math import *

# ? """ACTIVITÉ 1"""

def afficher_table_7() :
    for i in range(1, 11):
        resultat = 7 * i
        print("7 x", i, "=", resultat)


def affiche_bonjour():
    prenom = input("Entrer votre Prénom : ")
    print("Bonjour", prenom, "!")


def afficher_table_n(n):
    for i in range(1, 11):
        resultat = n * i
        print(f"{n} x {i} = {resultat}")

def affiche_salutation(a):
    prenom = input("Entrer votre Prénom : ")
    print(a, prenom, "!")

def Demande_Prenom_Nom():
    Prenom = input("Entrer votre Prénom : ")
    Nom = input("Entrer votre Nom : ")
    print("Bonjour", Prenom, Nom.upper(), "!")

# afficher_table_7()
# affiche_bonjour()
# afficher_table_n(5)
# affiche_salutation("Salut")
# Demande_Prenom_Nom()



# ? """ACTIVITÉ 2"""

def Trinome_x(Val_X):
    Equation = Val_X**2 + 7*Val_X + 4
    print("resultat d'équation =", Equation)

def Trinome_1(Val_A, Val_B, Val_C, Val_X):
    Equation = Val_A * Val_X**2 + Val_B * Val_X + Val_C
    print("resultat d'équation =", Equation)


def Conversion_Euro_Dollar(Val_Euro):
    Val_Dollar = Val_Euro * 1.15
    print(Val_Euro, "euros =", Val_Dollar, "dollars")

def Conversion_Euro_Devise(Val_Euro, Taux_Conversion, NomDevise2):
    Val_Devise = Val_Euro * Taux_Conversion
    print(Val_Euro, "euros =", Val_Devise, NomDevise2)

def Volume_Cube(Val_Cote):
    Volume = Val_Cote ** 3
    print("Le volume du cube est :", Volume, "unités cubiques pour un côté de", Val_Cote, "unités")

def Volume_Boule(Val_Rayon):
    Volume = (4/3) * math.pi * Val_Rayon ** 3
    print("Le volume de la boule est :", Volume, "unités cubiques pour un rayon de", Val_Rayon, "unités")


def Volume_Cylindre(Val_Rayon, Val_Hauteur):
    Volume = math.pi * Val_Rayon ** 2 * Val_Hauteur
    print("Le volume du cylindre est :", Volume, "unités cubiques pour un rayon de", Val_Rayon, "unités et une hauteur de", Val_Hauteur, "unités")

def Volume_Boite_Paralelipipedique(Val_Longueur, Val_Largeur, Val_Hauteur):
    Volume = Val_Longueur * Val_Largeur * Val_Hauteur
    print("Le volume de la boîte parallélépipédique rectangle est :", Volume, "unités cubiques pour une longueur de", Val_Longueur, "unités, une largeur de", Val_Largeur, "unités et une hauteur de", Val_Hauteur, "unités")

def Peri_Aire_Rectangle(Val_Longueur, Val_Largeur):
    Perimetre = 2 * (Val_Longueur + Val_Largeur)
    Aire = Val_Longueur * Val_Largeur
    print("Le périmètre du rectangle est :", Perimetre, "unités pour une longueur de", Val_Longueur, "unités et une largeur de", Val_Largeur, "unités")
    print("L'aire du rectangle est :", Aire, "unités carrées pour une longueur de", Val_Longueur, "unités et une largeur de", Val_Largeur, "unités")

def Peri_Aire_Cercle(Val_Rayon):
    Perimetre = 2 * math.pi * Val_Rayon
    Aire = math.pi * Val_Rayon ** 2
    print("Le périmètre du cercle est :", Perimetre, "unités pour un rayon de", Val_Rayon, "unités")
    print("L'aire du cercle est :", Aire, "unités carrées pour un rayon de", Val_Rayon, "unités")

def Conjecture_Aire_Sup_Peri():
    Compteur = 0
    Rayon = 0.0
    Aire = 0.0
    Perimetre = 0.0
    for i in range(0, 30):
        Rayon += 0.1
        Compteur += 1
        Peri_Aire_Cercle(Rayon)
    print("Au bout de", Compteur, "répétitions,", "on a une aire > périmetre du cerle avec une aire de ", Rayon)


# Trinome_x(7)
# Trinome_1(2, -1, 0, 6)
# Conversion_Euro_Dollar(100)
# Conversion_Euro_Devise(100, 0.85, "Francs Suisse")
# Volume_Cube(6)
# Volume_Boule(3)
# Volume_Cylindre(3, 5)
# Volume_Boite_Paralelipipedique(4, 5, 6)
# Peri_Aire_Rectangle(4, 5)
# Peri_Aire_Cercle(3)
# Conjecture_Aire_Sup_Peri()



# ? """ACTIVITÉ 3"""

def Triangle(taille):
    color("red")
    penup()
    goto(-300, -200)
    pendown()
    for _ in range(3):
        forward(taille)
        left(120)

def Carre(taille):
    color("green")
    penup()
    goto(0, 0)
    pendown()
    for i in range(4):
        forward(taille)
        left(90)

def Hexagone(taille):
    color("blue")
    penup()
    goto(150, -200)
    pendown()
    for i in range(6):
        forward(taille)
        left(60)

def Polygone(taille):
    Repetition = 8
    color("cyan")
    penup()
    goto(-300, 100)
    pendown()
    for i in range(Repetition):
        forward(taille)
        left(360 / Repetition)


# Triangle(200)
# Carre(200)
# Hexagone(100)
# Polygone(50)

# exitonclick()


# ? """ACTIVITÉ 4"""

def Reduction(Age):
    if Age < 10:
        print("Reduction de 50%")
    elif Age >= 10 and Age < 18:
        print("Reduction de 30%")
    elif Age >= 18 and Age < 60:
        print("Reduction de 0")
    elif Age >= 60:
        print("Reduction de 20%")


def Montant_Total_Famille(Prix):
    Nb_Personne = int(input("Entrez le nombre de personnes dans la famille : "))
    Montant_Total = 0   
    for i in range(Nb_Personne):
        Age_Personne = int(input(f"Entrez l'âge de la personne {i+1} : "))
        if Age_Personne < 10:
            Montant_Total += Prix * 0.5
        elif Age_Personne >= 10 and Age_Personne < 18:
            Montant_Total += Prix * 0.7
        elif Age_Personne >= 18 and Age_Personne < 60:
            Montant_Total += Prix
        elif Age_Personne >= 60:
            Montant_Total += Prix * 0.8
    print("Le montant total à payer pour la famille est :", Montant_Total, "euros")

def Calcul_Est_Exact(Val_A, Val_B, Reponse):
    if Val_A * Val_B == Reponse:
        print("La réponse est exacte !")
    else:
        print("La réponse est incorrecte. La bonne réponse est :", Val_A * Val_B)





# Reduction(19)
# Montant_Total_Famille(100)
Calcul_Est_Exact(5, 7, 35)