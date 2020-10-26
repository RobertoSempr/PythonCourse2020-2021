

punti = 0
risp = input("Mesi per anno?")
if risp == "12":
    print("Esatto!")
    punti = punti + 1
else:
    print("Sbagliato!")
risp = input("Giorni Dicembre?")
if risp == "31":
    print("Esatto!")
    punti = punti + 1
else:
    print("Sbagliato!")
print("Punteggio :", punti)



