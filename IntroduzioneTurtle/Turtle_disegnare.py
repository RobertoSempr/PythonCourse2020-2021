
import turtle

# -----------------------------------
# Creazione finestra
# -----------------------------------
finestra = turtle.Screen()
finestra.setup(600,600)
finestra.bgcolor("#994444")

# -----------------------------------
# Creazione penna
# -----------------------------------

penna = turtle.Turtle()
penna.color("blue")
#penna.color("blue", "red")


# -----------------------------------
# spostare la punta della penna
# -----------------------------------

penna.goto(-100,-100)

# -----------------------------------
# muovere la penna e disegnare quadrato
# -----------------------------------

# ciao
#penna.begin_fill()
penna.forward(100)
penna.left(90)
penna.forward(100)
penna.left(90)
penna.forward(100)
penna.left(90)
penna.forward(100)
#penna.end_fill()


# -----------------------------------
# pulire lo schermo
# -----------------------------------

#turtle.clearscreen()
#turtle.resetscreen()


# -----------------------------------
# disattivare la penna
# -----------------------------------

penna.penup()

# -----------------------------------
# spostare la punta della penna
# -----------------------------------

penna.goto(100,100)

# -----------------------------------
# riattivare la penna
# -----------------------------------

penna.pendown()

# -----------------------------------
# disegnare figura
# -----------------------------------

penna.speed(10)
for i in range(50):
    penna.forward(200)
    penna.left(150)



turtle.done()
