def stampa_tabellina(t):
    print("Ecco la tabellina del",t)
    for i in range(1,11):
        print(t,"moltiplicato per",i,"fa",t*i)

def somma_primi_numeri(t):
    somma = 0
    for i in range(1,t+1):
        somma = somma + i
    print("La somma finale da 1 a ",t,"vale",somma)




# ---------------------------
# inizio programma (main)
# ---------------------------
stampa_tabellina(123)
somma_primi_numeri(7654)
