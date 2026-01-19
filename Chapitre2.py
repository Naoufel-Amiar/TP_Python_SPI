import math
from turtle import *
from math import *
# ! Cours 1

# forward(100)
# left(90)
# forward(50)
# width(5)
# forward(100)
# color("red")
# right(90)
# forward(200)

# exitonclick()

# ? """ACTIVITÉ 1"""

# speed(0)
# width(3)

# # ========== P ==========
# penup()
# goto(-200, 0)
# setheading(90)
# pendown()

# forward(80)          # barre verticale
# right(90)
# forward(40)          # haut
# right(90)
# forward(40)          # descente demi-boucle
# right(90)
# forward(40)          # retour au milieu (boucle fermée)

# # ========== Y ==========
# # Point de jonction du Y (centre)
# penup()
# goto(-120, 40)
# setheading(0)
# pendown()

# # Branche vers le haut-droite
# setheading(60)
# forward(40)

# backward(40)

# # Branche vers le haut-gauche
# setheading(120)
# forward(40)

# # Revenir au centre
# backward(40)

# # Tige vers le bas
# setheading(270)
# forward(60)

# done()

# exitonclick()

# ? """ACTIVITÉ 2"""
speed(3)
width(3)
Taille_X_PentV1 = 100
Taille_X_PentV2 = 200

# Pentagone V1
def pentagone(taille):
    penup()
    goto(-300, -200)
    pendown()
    for i in range(5):
        forward(taille)
        left(72)

# Pentagone V2
def pentagone2(taille):
    penup()
    goto(100, 0)
    pendown()
    for i in range(5):
        forward(taille)
        left(72)

# Cercle

def Cercle(taille):
    penup()
    goto(-300, 0)
    pendown()
    for i in range(12):
        forward(taille)
        left(30)

def Escargot(taille):
    penup()
    goto(200, -200)
    pendown()
    forward(taille)
    left(30)
    for i in range(24):
        forward(taille)
        left(30)
        taille -= 5

# ? """ACTIVITÉ 4"""
def tracer_parabole():
    
    speed(0)
    width(2)
    color("blue")

    penup()
    x = -200
    y = (x**2) / 100
    goto(x, y)
    pendown()

    for x in range(-200, 201):
        y = (x**2) / 100
        goto(x, y)

def tracer_sinus():
    
    speed(0)
    width(2)
    color("red")

    penup()
    x = -200
    y = 100*math.sin(x/20)
    goto(x, y)
    pendown()

    for x in range(-200, 201):
        y = 100*math.sin(x/20)
        goto(x, y)

# ? """ACTIVITÉ 4"""
def triangle(t, taille):
    for _ in range(3):
        t.forward(taille)
        t.left(120)

def sierpinski(t, taille, niveau):
    if niveau == 0:
        triangle(t, taille)
    else:
        sierpinski(t, taille / 2, niveau - 1)
        t.forward(taille / 2)
        sierpinski(t, taille / 2, niveau - 1)
        t.backward(taille / 2)
        t.left(60)
        t.forward(taille / 2)
        t.right(60)
        sierpinski(t, taille / 2, niveau - 1)
        t.left(60)
        t.backward(taille / 2)
        t.right(60)

def tracer_sierpinski(niveau):
    screen = Screen()
    t = Turtle()
    t.speed(0)
    t.width(1)
    t.color("black")

    t.penup()
    t.goto(-200, -150)
    t.pendown()

    sierpinski(t, 400, niveau)
    done()

# ? """ACTIVITÉ 5"""
def dessiner_cercle(R):
    penup()
    goto(0, -R)
    setheading(0)
    pendown()
    circle(R)

def table_multiplication(k=2, N=12, R=200, afficher_points=True):
    speed(0)
    hideturtle()
    width(1)

    # 1) Cercle
    dessiner_cercle(R)

    # 2) Points sur le cercle
    points = []
    for i in range(N):
        angle = 2 * math.pi * i / N
        x = R * math.cos(angle)
        y = R * math.sin(angle)
        points.append((x, y))

        if afficher_points:
            penup()
            goto(x, y)
            dot(5)  # point

    # 3) Traits (table de k)
    for i in range(N):
        j = (k * i) % N
        penup()
        goto(points[i])
        pendown()
        goto(points[j])

# ? """ACTIVITÉ 6"""
def proche(tortues, seuil=8):
    xs = [t.xcor() for t in tortues]
    ys = [t.ycor() for t in tortues]
    return (max(xs) - min(xs) < seuil) and (max(ys) - min(ys) < seuil)

def spirale_poursuite_avec_segments(pas=4, iterations=5000, taille=200):
    screen = Screen()
    screen.title("4 tortues qui se poursuivent avec segments")
    screen.tracer(0, 0)

    # 4 tortues principales
    tortues = [Turtle() for _ in range(4)]
    couleurs = ["red", "blue", "orange", "green"]

    for t, c in zip(tortues, couleurs):
        t.color(c)
        t.speed(0)
        t.pensize(2)

    # Tortue dédiée aux segments
    seg = Turtle()
    seg.hideturtle()
    seg.speed(0)
    seg.pensize(1)
    seg.color("black")
    seg.penup()

    # Positions initiales (coins du carré)
    positions = [(-taille, -taille), (taille, -taille),
                 (taille, taille), (-taille, taille)]

    for t, pos in zip(tortues, positions):
        t.penup()
        t.goto(pos)
        t.pendown()

    # Boucle principale
    for _ in range(iterations):
        if proche(tortues):
            break
        # Trace les segments poursuivant → poursuivie
        for i in range(4):
            a = tortues[i].position()
            b = tortues[(i + 1) % 4].position()
            seg.goto(a)
            seg.pendown()
            seg.goto(b)
            seg.penup()

        # Déplacement des tortues
        for i in range(4):
            cible = tortues[(i + 1) % 4].position()
            tortues[i].setheading(tortues[i].towards(cible))
            tortues[i].forward(pas)

        screen.update()

    screen.mainloop()


# Lance l'expérience

# pentagone(Taille_X_PentV1)
# pentagone2(Taille_X_PentV2)
# Cercle(50)
# Escargot(130)
# tracer_parabole()
# tracer_sinus()

#tracer_sierpinski(3)  # 0 / 1 / 2 / 3

#table_multiplication(k=2, N=200, R=250, afficher_points=True)

spirale_poursuite_avec_segments()

exitonclick()