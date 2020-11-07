def stampaTabellina(numero):
    # questa procedura riceve un numero come parametro
    # e stampa la tabellina corrispondente
    print("Ecco la tabellina del ", numero)
    for i in range(1, 11):
        print(i*numero)


# chiedo un numero e genero la sua tabellina
numero = input("Dammi un numero: ") # chiedo un numero 
numero = int(numero)                # trasformo il testo in numero vero
stampaTabellina(numero)             # chiamo la procedura

# proviamo di nuovo
numero = input("Dammi un numero: ") # chiedo un numero 
numero = int(numero)                # trasformo il testo in numero vero
stampaTabellina(numero)             # chiamo la procedura

# proviamo con le prime 5 tabelline
for j in range (5):
    stampaTabellina(j+1)
