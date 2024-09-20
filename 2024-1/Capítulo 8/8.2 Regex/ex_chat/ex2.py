#validar enderenços de email 

import re 
teste = "teste@dominio.com"
teste2 = "test@com"

def email():
    return bool(re.fullmatch(r"[a-zA-Z0-9._%+-]+@\w+\.[a-zA-Z]{2,}", teste))

print(email())