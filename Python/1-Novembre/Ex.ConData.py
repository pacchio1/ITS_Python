######	Marco Pacchiotti 016	######
# utilizzo di date in python
import calendar
import datetime
from datetime import date
from datetime import time
from datetime import datetime
oggi = date.today()
print(oggi)
anno = oggi.year
mese = oggi.month
giorno = oggi.day
print("dd", giorno, "mm", mese, "yyyy", anno)
data = date(2002, 11, 9)
print(data.strftime("%d/%m/%Y %H:%M:%S"))
print(oggi - data)
# print(calendar.calendar(2023))#importa caledario 2023
# calcolo distanza a compleanno
compleanno = date(2023, int(input("mese nascita:")),
                  int(input("giorno di nascita:")))
if compleanno.month > oggi.month:
    compleanno = date(2022, compleanno.month, compleanno.day)
    print(compleanno-oggi)
else:
    print(compleanno-oggi)
# scadenza
scadenza = datetime(int(input("anno scadenza:")), int(input("mese scadenza:")), int(input(
    "giorno di scadenza:")), int(input("ora scadenza:")), int(input("minuto scadenza:")), 0)
now = datetime.now()
print(scadenza-now)
