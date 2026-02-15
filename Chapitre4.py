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

def Test_multiplication( Val_A, Val_B, Language):
    if Language == "Français":
        Reponse = int(input(f"Quel est le résultat de la multiplication de {Val_A} par {Val_B} ? "))
        if Val_A * Val_B == Reponse:
            print("Bravo ! La réponse est correcte.")
        else:
            print("Désolé, la réponse est incorrecte.")
            print(f"Le résultat de la multiplication de {Val_A} par {Val_B} est : {Val_A * Val_B}")
    elif Language == "Anglais":
        Reponse = int(input(f"What is the result of multiplying {Val_A} by {Val_B}? "))
        if Val_A * Val_B == Reponse:
            print("Congratulations! The answer is correct.")
        else:
            print("Sorry, the answer is incorrect.")
            print(f"The result of multiplying {Val_A} by {Val_B} is: {Val_A * Val_B}")


# ? """ACTIVITÉ 4"""

def Valeur_Absolue(Val):
    if Val < 0:
        print("La valeur absolue de", Val, "est", -Val)
    else:
        print("La valeur absolue de", Val, "est", Val)

def Racine_De_Carre(Val):
    print("La racine carrée de", Val, "est", math.sqrt(Val**2))

def Egalité_ValAbso_RaciCarre(Val):
    if Valeur_Absolue(Val) == Racine_De_Carre(Val):
        print("La valeur absolue de", Val, "est égale à la racine carrée de", Val, "au carré.")
    else:
        print("La valeur absolue de", Val, "n'est pas égale à la racine carrée de", Val, "au carré.")

def F1(Val_A, Val_B):
    Calcul = (Val_A + Val_B) ** 2
    print("Le résultat de F1 est :", Calcul)
    return Calcul

def F2(Val_A, Val_B):
    Calcul = Val_A ** 2 + 2*Val_A*Val_B + Val_B**2
    print("Le résultat de F2 est :", Calcul)
    return Calcul

def F1_1(Val_A, Val_B):
    Calcul = (Val_A - Val_B) ** 3
    print("Le résultat de F1_1 est :", Calcul)
    return Calcul

def F2_1(Val_A, Val_B):
    Calcul = Val_A ** 3 - 3*Val_A**2*Val_B - 3*Val_A*Val_B**2 + Val_B**3
    print("Le résultat de F2_1 est :", Calcul)
    return Calcul

def F1_2(Val_A, Val_B):
    Calcul = (Val_A - Val_B) ** 3
    print("Le résultat de F1_2 est :", Calcul)
    return Calcul

def F2_2(Val_A, Val_B):
    Calcul = Val_A ** 3 - 3*Val_A**2*Val_B + 3*Val_A*Val_B**2 - Val_B**3
    print("Le résultat de F2_2 est :", Calcul)
    return Calcul

def Verif_F1_F2(Val_A, Val_B):
    for i in range (-100, 101):
        Val_A = i
        for j in range (-100, 101):
            Val_B = j
            if F1(Val_A, Val_B) != F2(Val_A, Val_B):
                print("F1 et F2 ne sont pas égales pour A =", Val_A, "et B =", Val_B)
    print("F1 et F2 sont égales pour tous les entiers de -100 à 100.")

def Verif_F1_1_F2_1():
    egalite = True
    for i in range(-100, 101):
        for j in range(-100, 101):
            if F1_1(i, j) != F2_1(i, j):
                print("Pas égales pour A =", i, "B =", j)
                egalite = False
    if egalite:
        print("Elles sont égales pour tous les entiers.")

def Verif_F1_2_F2_2():
    egalite = True
    for i in range(-100, 101):
        for j in range(-100, 101):
            if F1_2(i, j) != F2_2(i, j):
                print("Pas égales pour A =", i, "B =", j)
                egalite = False
    if egalite:
        print("Elles sont égales pour tous les entiers.")


def SinCos(Val_X):
    Calcul = math.sin(Val_X) ** 2 + math.cos(Val_X) ** 2
    print("Le résultat de SinCos est :", Calcul)
    return Calcul

def Verif_SinCos_Simple(Val_X):
    if SinCos(Val_X) != 1:
        print("SinCos n'est pas égal à 1 pour X =", Val_X)
    else:
        print("SinCos est égal à 1 pour X =", Val_X)




# Reduction(19)
# Montant_Total_Famille(100)
# Calcul_Est_Exact(5, 7, 35)
# Test_multiplication(5, 7, "Français")
# Test_multiplication(5, 7, "Anglais")
# Valeur_Absolue(10)
# Racine_De_Carre(-5)
# Egalité_ValAbso_RaciCarre(-5)
# Verif_F1_F2(0, 0)
# Verif_F1_1_F2_1()
# Verif_F1_2_F2_2() 
# ! """En Compararant, on remarque que pour tous les entiers de -100 à 100, F1_2 et F2_2 sont égales, ce qui confirme l'identité remarquable (a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3.""")

Verif_SinCos_Simple(36)
