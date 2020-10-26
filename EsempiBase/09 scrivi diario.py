


import datetime
# nome file da scrivere
nomeFile = "diario.txt"
# 'a' = append (in fondo)
mioFile = open(nomeFile, 'a')
riga = input("Cosa scrivi?")
# scrivo data e ora
s=str(datetime.datetime.now())
mioFile.write(s + '\n')
# la riga 
mioFile.write(riga + '\n')
# chiudo il file
mioFile.close()


