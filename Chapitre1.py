import math

# ? """ACTIVITÉ 1"""

# ! Cours 1
# Partie 1
Nb_Seconde_1_Annee = 365 * 24 * 60 * 60
Nb_Seconde_1_Siecle = 100 * Nb_Seconde_1_Annee
print("Nombre de secondes dans un siècle :", Nb_Seconde_1_Siecle)


# Partie 2
Plus_Que_1_Milliard = (1+2)*(3+4)*(5+6)*(7+8)*(9+10)*(11+12)*(13+14)*(15+16)
print("Nombre d'années pour atteindre un milliard de secondes :", Plus_Que_1_Milliard)


# Partie 3
Calcul_3_Last_Chiffres = 123456789**7
print("Les 3 derniers chiffres de 123456789^7 sont :", Calcul_3_Last_Chiffres % 1000)


# ! Cours 2
print("2+2 = ",2+2)
print("Bonjour tout le monde!")

# ! Cours 3
# ? """ACTIVITÉ 2"""
#1.a
B = 7
b = 4
h = 3
Calcul_aire_trapeze = (B + b) * h / 2
print("L'aire du trapèze est de :", Calcul_aire_trapeze)


#1.b
L = 10
l = 8
h = 3

Calcul_aire_Boite = L*l*h
print("Le volume de la boîte est de :", Calcul_aire_Boite)


#1.c
R = 10
calcul_Aire_disque = 3.14 * R**2
print("L'aire du disque est de :", calcul_Aire_disque)


#2.
x = 7
y = 2*x
y = y-1
x = x+3*y
print("La valeur de x est :", x)


#3. 
Capital = 1000
taux_interet = 1.1
nb_année = 3

Montant_final = Capital * taux_interet**nb_année
print("Le montant final après intérêts est de :", Montant_final)


#4.
a = 9
b = 11
c = 0

c = a
a = b
b = c
print("La valeur de a est :", a)
print("La valeur de b est :", b)


# ! Cours 4
# ? """ACTIVITÉ 3"""

#1.
a = 10403
b = 10506

ppcm = math.gcd(a, b)
print("Le PPCM de", a, "et", b, "est :", ppcm)


#2.
x = 3.9

ABS = abs(x**2 - 15)
ROUND = round(2*x)
FLOOR = math.floor(3*x)
print("Les résultats des fonctions mathématiques sont calculés.")
print("ABS :", ABS)
print("ROUND :", ROUND)
print("FLOOR :", FLOOR)


#2.
calcul = math.cos(math.pi/7)**2 + math.sin(math.pi/7)**2
print("Le calcul trigonométrique donne :", calcul) # TODO: Ca marche, on a le 1 en résultat.


# ! Cours 5

# ? """ACTIVITÉ 4"""
