
# ? """ACTIVITÉ 1"""
def Quotien_Reste():
    VerifReste = False
    VerifEgalite = False
    Val_A = int(input("Entrez la valeur de A : "))
    while Val_A <= 0:
        print("Veuillez entrer une valeur positive pour A.")
        Val_A = int(input("Entrez la valeur de A : "))
    Val_B = int(input("Entrez la valeur de B : "))
    while Val_B < 0:
        print("Veuillez entrer une valeur positive pour B.")
        Val_B = int(input("Entrez la valeur de B : "))
    Quotien = Val_A // Val_B
    Reste = Val_A % Val_B
    if Reste >= 0 and Reste < Val_B:
        VerifReste = True 
        print("Verification du reste <= Reste < Val_B :", VerifReste)
    if Val_A == Quotien * Val_B + Reste: 
        VerifEgalite = True
        print("Verification de l'égalité A = Quotien * Val_B + Reste :", VerifEgalite)

    print("Le quotient de", Val_A, "divisé par", Val_B, "est :", Quotien)
    print("Le reste de", Val_A, "divisé par", Val_B, "est :", Reste)

def Est_Pair(Val):
    if Val % 2 == 0:
        print("Le nombre", Val, "est pair.")
    else:
        print("Le nombre", Val, "est impair.")

def Est_Divisible(Val_A, Val_B):
    if Val_B == 0:
        print("La division par zéro n'est pas définie.")
    elif Val_A % Val_B == 0:
        print("Le nombre", Val_A, "est divisible par", Val_B)
    else:
        print("Le nombre", Val_A, "n'est pas divisible par", Val_B)



# Quotien_Reste()
# Est_Pair(6)
# Est_Divisible(10, 2)
# Est_Divisible(10, 3)


# ? """ACTIVITÉ 1"""

def Plus_Petit_Diviseur(Val):
    if Val < 2:
        print("Veuillez entrer un entier supérieur ou égal à 2.")