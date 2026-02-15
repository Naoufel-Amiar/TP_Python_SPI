import math

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



# ? """ACTIVITÉ 2"""

