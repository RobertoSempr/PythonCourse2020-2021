
# prima di esaminare il codice, proviamo a ragionare insieme:
# ------------------------------------------------------------
# cosa voglio fare?
# ------------------------------------------------------------
# voglio uno script che, dato un elenco di proverbi,
# mi scelga e stampi un proverbio a caso, quando lo lancio
# ------------------------------------------------------------
# come posso farlo ?
# - devo definire, utilizzando un vettore, l'elenco dei proverbi
# - mi serve qualcosa che possa generare un numero a caso
# - e poi?
# ------------------------------------------------------------






































# mi serve per poter generare numeri casuali
import random

# definisco il vettore (qui si chiama lista) con l'elenco dei proverbi disponibili
v_proverbi = [
    "Il mattino ha l'oro in bocca",
    "Finchè la barca va, lasciala andare",
    "Chi fa da sè fa per tre"
    ]

# calcolo il numero di proverbi disponibili
numero_proverbi = len(v_proverbi)

# genero un numero di posizione casuale nel vettore dei proverbi
posizione_casuale = random.randint(0, numero_proverbi-1)

# stampo il risultato
print("Ecco il proverbio del giorno:")
print(v_proverbi[posizione_casuale])
