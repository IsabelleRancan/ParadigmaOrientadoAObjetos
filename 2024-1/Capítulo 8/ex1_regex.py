#Na língua portuguesa, palavras no plural terminam com “s”. Receber uma string e retornar uma lista com as palavras que terminam com “s”.
import re

def plural():
    return re.findall(r"\b\w+s\b", "palavras que tens s no fim palavras") #usar * se quiser mostrar o s sozinho 

#\b para 'quebrar' as palavras, \w pra exibir alphanuméricos, + pra exibir palavras que tenham s+pelo menos 1 caractere, 
# s\b letra s no final de cada palavra

print(plural())