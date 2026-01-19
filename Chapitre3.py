import random
a = random.randint(1, 12)
b = random.randint(1, 12)

Calcul = a*b

reponse_proposee = int(input("Quelle est le résultat de la multiplication de {} par {} ? ".format(a, b)))


if reponse_proposee == Calcul:
    print("Bravo ! La réponse est correcte.")
else:
    print("Désolé, la réponse est incorrecte.")
    print("Le résultat de la multiplication de", a, "par", b, "est :", Calcul)