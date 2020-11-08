def somma_primi_numeri(t):
    somma = 0
    for i in range(1,t+1):
        somma = somma + i
    return somma


   



# inizio del programma
x = somma_primi_numeri(100)
print("La somma finale da 1 a 100 vale",x)
x = somma_primi_numeri(1000)
print("La somma finale da 1 a 1000 vale",x)
x = somma_primi_numeri(1234)
print("La somma finale da 1 a 1234 vale",x)
