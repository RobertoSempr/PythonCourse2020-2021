import time

def aspetta(secondi):
    print(secondi)
    while secondi > 0 :
        time.sleep(1)
        secondi = secondi - 1
        print(secondi)

aspetta(5)
print("Boom!")
aspetta(4)
print("Bip!")
aspetta(3)
print("Gulp!!!!")

input("'Invio' per chiudere!")

exit()
