# Receber uma string e retornar True caso seja um horário no formato “HH:MM” válido, ou False caso contrário. 
# Usar apenas uma expressão regular que faça a validação completa.

import re

def hora():
    return bool (re.fullmatch(r"\b(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])\b", "03:35")) #\d corresponde a qualquer digito de 0-9

print(hora())