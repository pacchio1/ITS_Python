def elimina_duplicati(lista):
    # Converte la lista in un insieme per eliminare i duplicati
    senza_duplicati = set(lista)
    # Converte nuovamente l'insieme in una lista e ritorna il risultato
    return list(senza_duplicati)


# Esempio di utilizzo
lista = [1, 2, 3, 1, 2, 3, 4, 5, 6, 4,
         5, 6, 7, 13, 6, 10, 8, 5, 6, 4,
         5, 7, 1, 9, 11, 23, 12, 14, 7,
         1, 15, 16, 17, 18, 19, 20, 21, 22, 23,
         24, 25, 26, 27, 28, 29, 8, 30, 6, 4]
lista_senza_duplicati = elimina_duplicati(lista)
print(lista_senza_duplicati)  # stampa [1, 2, 3]
