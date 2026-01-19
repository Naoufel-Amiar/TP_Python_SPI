
##############################
# Premiers pas
##############################

##############################
# Activité 1 - Nombres
##############################

#%%
##############################
# Cours 1
#print("--- Cours ---")
# Afficher une phrase
#print("Bonjour le monde !")

# Addition
5+7
#print(5+7)

# Multiplication
#print(6*7)

#print(3*(12+5))

#print(3*1.5)

# Puissance

#print(3**2)

#print(10**-3)

# Division réelle

#print(14/4)

#print(1/3)

# Division entière et modulo

#print(14//4)

#print(14%4)


#%%
##############################
# Questions

# Q1
# Nombre de secondes dans un siècle
print("--- Question 1 ---")

Q1_CalCulTempsiecle = 100 * 365 * 24 * 60 * 60
print("Il y a", Q1_CalCulTempsiecle, "secondes dans un siècle.")


# Q2 
# A partir dans quand plus grand qu'un milliard
print("--- Question 2 ---")

Q2_CalCulTempsMilliard = 10**9 / (60 * 60 * 24 * 365)
print("Il faut partir dans environ", round(Q2_CalCulTempsMilliard, 2), "ans pour dépenser un milliard d'euros à raison de 1 euro par seconde")


# Q3
# Trois derniers chiffres de 123456789 * 123456789 * ...
print("--- Question 3 ---")



# Q4
# Premier 1/n avec période 7
print("--- Question 4 ---"), 
print("Le le premier entier dont l’inverse a une écriture décimale périodique de longueur 7 est entre 230 et 240 ")



# Q5
# Trouver un nb connaissant deux divisions et un reste
print("--- Question 5 ---")

#%%
##############################
# Premiers pas
##############################


##############################
# Activité 2 - Variables
##############################


##############################
# Cours 2

# C1 - variables

a = 3  # Une variable
b = 5  # Une autre variable

print("La somme vaut",a+b)   # Affiche la somme
print("Le produit vaut",a*b) # Affiche le produit

c = b**a     # Nouvelle variable...
print(c)     # ... qui s'affiche


# C2 - aire d'un triangle

base = 8
hauteur = 3
aire = base * hauteur / 2
print(aire)
# print(Aire)  # !! Erreur !!


# C3 - ajout

S = 1000
S = S + 100
S = S + 200
S = S - 50
print(S)

#%%
##############################
# Questions

# Q1

# Aires - Volumes

# Trapèze : bien nommé les choses



# Boîtes



# Boules



# Q2 
# Remettre dans l'ordre de sorte qu'à la fin x = 46





# Q3
# Intérêts de 10%




# Q4 


# Bon choix afin d'échanger a et b

# Mauvais




# Mauvais




# Mauvais






# Bon




#%%
##############################
# Premiers pas
##############################


##############################
# Activité 3 - Utiliser des fonctions
##############################


##############################
# Cours 3

# C1 - fonctions

print("Coucou")

x = float("+1.234567")
print(x)


# C2 - module math

from math import *

x = sqrt(2)
print(x)
print(x**2)

# C3 - fonction trigo

angle = pi/2
print(angle)
print(sin(angle))


# C4 - décimal vers entier

x = 3.6
print(round(x))
print(floor(x))
print(ceil(x))


#%%
##############################
# Questions

# Q1
# pgcd




# Q2
# Valeur absolue (entre 3.50 et 4 avec un pas de 0.05)




# Q3
# Angle










#%%
##############################
# Premiers pas
##############################


from math import *


##############################
# Activité 4 - Boucle "pour"
##############################

##############################
# Cours 5

# C1 - Boucle "for"

for i in range(10):
    print(i*i)


# C2 - Boucle "for"

somme = 0
for i in range(20):
    somme = somme + i
print(somme)


# C3

print(list(range(10)))
print(list(range(10,20)))
print(list(range(10,20,2)))   


# C4 - Imbrication de boucles

for x in [10,20,30,40,50]:
    for y in [3,7]:
        print(x+y)

##############################
# Questions

# Q1 
# Cubes







# Q2
# Puissances de 2



# Q3
# Minimum d'une fonction par balayage






# Q4
# Volume d'une boule qui vaut 100
   




#%%


##############################
# Premiers pas
##############################


##############################
# Activité 5 - Boucle "pour" (suite)
##############################

# Questions

# Q1
# Sommes des carrés




# Q2
# Produits





# Q3
# Tables de multiplications






