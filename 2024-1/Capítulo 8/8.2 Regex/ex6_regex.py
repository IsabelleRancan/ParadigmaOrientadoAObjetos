#Receber uma string contendo informações sobre filmes e retornar uma lista apenas com os títulos dos filmes produzidos antes de 1990. 
import re

def filmes_antes_de_1990(string_filmes):
    # Regex para capturar o título do filme e o ano entre parênteses
    filmes = re.findall(r'([A-Za-z\s]+)\s\((\d{4})\)', string_filmes)
    
    # Filtrar apenas os filmes antes de 1990
    filmes_antes_1990 = [titulo for titulo, ano in filmes if int(ano) < 1990]
    
    return filmes_antes_1990

# Exemplo de string de entrada
string_filmes = "Back to the Future (1985), The Matrix (1999), Star Wars (1977), Titanic (1997), Blade Runner (1982)"

# Chamando a função e imprimindo o resultado
result = filmes_antes_de_1990(string_filmes)
print(result)

