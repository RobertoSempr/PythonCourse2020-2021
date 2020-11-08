def somma_primi_numeri(t):
    somma = 0
    for i in range(1,t+1):
        somma = somma + i
    print("La somma finale da 1 a ",t,"vale",somma)



# inizio del programma
somma_primi_numeri(100)
somma_primi_numeri(1000)
somma_primi_numeri(1234)
