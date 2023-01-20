"""
from platform import platform,machine,processor,system,version,python_implementation,python_version_tuple
print(platform())
print(machine())
print(processor())
print(system(),version())
print(python_implementation(),python_version_tuple())
"""

"""
############ Cartelle ############
import os
cartella=os.getcwd()
print(cartella)
#file#
for nome in os.listdir():
    print(nome)
try:
    os.mkdir("test_cartella")
except:
    os.rmdir("test_cartella")
"""

####GUI####
from tkinter import filedialog
import os
nome_file=filedialog.askopenfilename(filetypes=(("file di testo","*.txt"),("Tutti i file","*.*")))
print(nome_file)
stream=open(nome_file,mode="r",encoding="utf-8")
st=stream.read()
print(st)
stream.close()
stream=open("test_file.txt",mode="w",encoding="utf-8")
stream.write(st)
stream.close()
