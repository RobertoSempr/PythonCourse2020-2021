
# mi faccio dire un numero
x = input("Dammi un numero da elaborare: ")

# devo convertire il testo acquisito in un numero
x = int(x)

# preparo la variabile che contiene la somma
somma = 0

# devo 'iterare', fare un ciclo
while x > 0:
    somma += x # sommo il valore di x al totale
    x  -= 1    # decremento di uno il valore di x

# trasformo in testo le variabili necessarie
x = str(x)
somma = str(somma)

# stampo il risultato
messaggio = "La somma dei numeri da 0 a " + x + " vale: " + somma
print(messaggio)
