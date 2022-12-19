# valuta
print("calcola conversione euro in dolari/lire")
# euro
euro = float(input("Euro :"))
print("Dollari =", str(euro*1.0330), "|Lire =", str(euro*1936.27))
# lire
lire = float(input("lire :"))
print("Dollari =", str(lire/1936.27*1.0330), "|euro =", str(lire/1936.27))
# dollari
dolari = float(input("dollari :"))
print("lire =", str(dolari/1.0330*1936.27), "|euro =", str(dolari/1.0330))
