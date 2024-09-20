#extrair # 
import re
texto = "Adoro #programação e #regex são #muito_legais!"

def extraindo():
    return re.findall(r"\#\w+", texto) #(r"\b(?<=\#)\w*", texto)-> rotorna as palavras sem a #

print(extraindo())