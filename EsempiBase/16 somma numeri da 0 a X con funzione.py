def somma(numero):
    calcolo = 0
    while numero > 0:
        calcolo += numero
        numero  -= 1
    return calcolo


x = int(input("Dammi un numero da elaborare: "))

y = somma(x)

print("La somma dei numeri da 0 a ", x , " vale: ", y)
