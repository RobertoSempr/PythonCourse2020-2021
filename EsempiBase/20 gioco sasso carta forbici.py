import random
import os

def partita():

    # -----------------------------------
    # procedura che simula una partita
    # -----------------------------------

    # definizione dell'elenco delle mosse (in una lista)
    v = [
        "sasso",
        "carta",
        "forbici"
        ]

    # messaggio di benvenuto
    print("---------------------------------------------------")
    print("Benvenuto a 'sasso, carta, forbici!'")
    print("---------------------------------------------------")

    # genero un numero a caso e prendo un elemento a caso
    # nella lista delle mosse
    numero = random.randint(0,2)
    scelta = v[numero]

    # chiediamo al giocatore che mossa sceglie
    giocatore = input("sasso, carta o forbici? ")

    # ora possiamo far sapere al giocatore che mossa ha scelto il computer
    print("Io ho scelto ", scelta)

    # situazioni in cui si ha un pareggio
    if giocatore == scelta:
        messaggio = "Nessuno vince ..."

    # dobbiamo ora capire chi ha vinto ...
      
    # situazioni in cui vince il giocatore
    elif giocatore == "sasso"   and scelta == "forbici":
        messaggio = "Hai vinto !!!"
    elif giocatore == "carta"   and scelta == "sasso":
        messaggio = "Hai vinto !!!"
    elif giocatore == "forbici" and scelta == "carta":
        messaggio = "Hai vinto !!!"
        
    #situazioni in cui vince il computer
    elif scelta == "carta"   and giocatore == "sasso":
        messaggio = "Ho vinto io!"
    elif scelta == "forbici" and giocatore == "carta":
        messaggio = "Ho vinto io!"
    elif scelta == "sasso"   and giocatore == "forbici":
        messaggio = "Ho vinto io!"

    # situazioni in cui il giocatore non ha scritto bene
    else:
        messaggio = "Non ho capito ..."

    # stampiamo il messaggio con l'esito dello scontro
    print("") # riga vuota
    print(messaggio)

# ------------------------------------------
# inizio script
# ------------------------------------------

# assegno la variabile che contiene la condizione per uscire
continua = True

# loop per lanciare una nuova sfida
while continua:
    partita()
    if input("Vuoi fare un'altra partita? (s/n) ") != "s":
        continua = False

# alla fine del gioco ...
print("Grazie per avermi sfidato, torna presto!")
