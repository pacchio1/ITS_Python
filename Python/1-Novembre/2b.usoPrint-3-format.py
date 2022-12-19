a = 10
b = 15
x = "io sono {} {}".format('Mario', 'Rossi')
print(x, "digente da %d anni e lavoro da %d " % (a, b), "anni")
data = '20/04/1980'
eta = 25

print(f"data nascita {data} età: {eta}")
print(f"data nascita {data} età: {eta:2.3f}")
print("data nascita {} età: {}".format(data, eta))
print("data nascita {1} età: {0}".format(eta, data))
print("data nascita {d} età: {e}".format(e=eta, d=data))
print("data nascita {0:} età: {1:2.3f}".format(data, eta))
"""
**** Stampa  ***
ARTICOLO	PREZZO 	QUANTITA	SCONTO APPLICATO 	TOTALE SCONTATO  
Pomodori	5.23 	25		    23.46			    107,41 Euro
"""
nome = "Pomodori"
prezzo = 5.23455
quantita = 25
sc = 23.4567
tot = prezzo*quantita
txt = "{:.<20} {:<7} {:<10} {:<18} {:<6}"
print(txt.format("ARTICOLO", "PREZZO", "QUANTITA",
      "SCONTO APPLICATO ", "TOTALE SCONTATO"))
txt = "{:.<20} {:<7} {:<10} {:<18} {:<6}"
print(txt.format(nome, str(round(prezzo, 2)), str(
    quantita), str(round(sc, 2)), str(round(tot-sc, 2))))
