#verificar um número de telefone 

import re 

teste = '(11) 98765-4321'
teste2 = '1234-5678'

def telefone():
    return bool (re.fullmatch(r"\(\d{2}\)\s\d{5}-\d{4}", teste))

print(telefone())