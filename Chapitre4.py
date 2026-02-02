
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


# Trinome_x(7)
Trinome_1(2, -1, 0, 6)