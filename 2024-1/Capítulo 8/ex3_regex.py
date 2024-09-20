# Receber uma string com várias linhas e retornar uma lista com todas as datas no formato dd/mm/aaaa.

import re

texto = """06/05/2004 é o dia que eu nasci \n e 25/12/2024 é natal"""

def datas():
    return re.findall(r'\b\d{2}/\d{2}/\d{4}\b', texto) #\b inicio, \d qualquer digito, {2}com duas casas


print(datas())