#Receber uma string e retornar uma lista com as palavras que contém duas letras repetidas consecutivas, como “correr” ou “assado”.
import re 

def repetidas():
    return re.findall(r"\b\w*(\w)\1+\w*\b", "assado suco cassa carrossel")

print(repetidas())



#import re

#def repetidas(texto):
    ## Expressão regex para capturar palavras com duas letras repetidas consecutivas
#    return [match.group() for match in re.finditer(r"\b\w*(\w)\1\w*\b", texto)]

#print(repetidas("assado suco cassa carrossel"))
