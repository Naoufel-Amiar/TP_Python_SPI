import turtle
import random

# ? """ACTIVITÉ 1"""
def guess_calcul():
    a = random.randint(1, 12)
    b = random.randint(1, 12)

    Calcul = a*b

    reponse_proposee = int(input("Quelle est le résultat de la multiplication de {} par {} ? ".format(a, b)))


    if reponse_proposee == Calcul:
        print("Bravo ! La réponse est correcte.")
    else:
        print("Désolé, la réponse est incorrecte.")
        print("Le résultat de la multiplication de", a, "par", b, "est :", Calcul)

# ? """ACTIVITÉ 2"""
def interprete(mot):
    turtle.speed(0)
    turtle.width(2)

    for c in mot:
        if c == "A":
            turtle.pendown()
            turtle.forward(100)

        elif c == "a":
            turtle.penup()
            turtle.forward(100)

        elif c == "g":
            turtle.left(90)

        elif c == "d":
            turtle.right(90)
    turtle.exitonclick()

# Exemple donné
mot = "AagAgAdAgAAgaAA"

# ? """ACTIVITÉ 3"""


for d in range(100):
    for u in range(10):
        nombre = 10*d + u
        print(nombre)
print("\n")


for d in range(100):
    for u in range(10):
        nombre = 10*d + u

        if nombre == 0:
            continue

        unite = nombre % 10
        dizaine = (nombre // 10) % 10
        centaine = nombre // 100

        if unite == 3 and (unite + dizaine + centaine) == 15 and dizaine % 2 == 0:
            print("une des solutions est:", nombre)



# ? """ACTIVITÉ 4"""
print("-------C<=B<=A-------")
print("\n")
print("Veuillez entrer trois valeurs entières A, B et C :")
print("\n")
Val_A = int(input("Entrez la valeur de A : "))
Val_B = int(input("Entrez la valeur de B : "))
Val_C = int(input("Entrez la valeur de C : "))

if Val_A <= Val_B <= Val_C:
    print("La condition A ≤ B ≤ C est validé")
else:
    print("La condition A ≤ B ≤ C n'est pas validé")
if Val_A + Val_B >= Val_C:
    print("Il existe bien un triangle avec ces trois valeurs")
else:
    print("Il n'existe pas de triangle avec ces trois valeurs")

if Val_A**2 + Val_B**2 == Val_C**2:
    print("Le triangle est rectangle")
else:
    print("Le triangle n'est pas rectangle")
# ? """ACTIVITÉ 5"""




#guess_calcul()
#interprete(mot)
