#Receber uma string e retornar uma lista com as palavras que contém duas letras repetidas consecutivas, como “correr” ou “assado”.
import re 

def repetidas():
    return re.findall(r"\b\w{2}", "assado suco cassa carrossel")

print(repetidas())