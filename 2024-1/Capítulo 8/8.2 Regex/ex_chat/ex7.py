#validar data 
#DD/MM/YYYY, onde o dia vai de 01 a 31, o mês de 01 a 12 e o ano tem quatro dígitos.
import re 
texto = "25/12/2020"
texto2 = "32/13/2020"

def validar():
    return bool (re.fullmatch(r"(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[12])/\d{4}", texto))

print(validar())