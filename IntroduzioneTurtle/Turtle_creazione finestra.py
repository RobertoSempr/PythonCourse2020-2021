

import turtle

# ------------------------------------------------------------------------
#creazione finestra, grandezza, e posizionamento sullo schermo
# la posizione x=0 y=0 corrisponde al punto in alto a destra dello schermo
# ------------------------------------------------------------------------
finestra = turtle.Screen()
finestra.setup(600,600)
#finestra.setup(600,600, startx=0, starty=0)
finestra.title("Finestra di prova")

# -----------------------------------------------------------------------
# impostazione colore di sottofondo
# -----------------------------------------------------------------------

#finestra.bgcolor("#994444")
finestra.bgcolor(0,0,0)

# -----------------------------------------------------------------------
#impostazione di imamgine di sottofondo
#l'immagine deve essere in formato "gif" e risisiedere nella stessa directory
#controllare che le dimensioni dell'immaggine in pixel siano cotenibili nella finestra,
#altrimenti adattare la finestra
# -----------------------------------------------------------------------

finestra.bgpic("FG_logo.gif")
#finestra.bgpic("SW_image.gif")

# -----------------------------------------------------------------------
#chiudere finestra con un click su qualunque punto della finestra
# -----------------------------------------------------------------------

turtle.exitonclick()

# -----------------------------------------------------------------------
#chiusura finestra automatica
# -----------------------------------------------------------------------
#turtle.bye()



