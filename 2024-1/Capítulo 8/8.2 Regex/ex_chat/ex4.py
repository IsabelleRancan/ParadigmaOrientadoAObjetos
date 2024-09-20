#retorna todas as palavras começadas com maiúscula
import re 
texto = "João e Maria foram ao Parque Central."

def maiusculas():
    return re.findall(r"\b([A-Z]\w*)", texto)

print(maiusculas())