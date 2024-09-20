#extrair números de um texto 

import re 
texto = "Eu tenho 2 gatos e 3 cachorros"

def numeros():
    return re.findall(r"\d", texto)

print(numeros())