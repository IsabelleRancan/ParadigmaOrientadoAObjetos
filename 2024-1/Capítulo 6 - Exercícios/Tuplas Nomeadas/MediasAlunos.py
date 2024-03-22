from collections import namedtuple

# 2 - Escreva uma função que receba uma lista de tuplas nomeadas representando alunos e retorne a média de suas notas

#criando a tupla nomeada com os parêmetros necessários 
Aluno = namedtuple("Aluno",["Nome", "Idade", "Nota"])

def calculando_media(lista_de_alunos):
    """"Criando a função que vai calcular a média. O nome do parâmetro passado não é relevante, 
    é apenas para destacar o fato de que a função receberá a lista"""

    soma_notas = 0 #variável para criar a soma de todas as notas

    for aluno in lista_de_alunos: #criando um foreach para iterar a tupla e procurar as notas dos alunos
        soma_notas += aluno.Nota 

    media_notas = soma_notas / (len (lista_de_alunos)) #calculando a media 
    return media_notas

#TESTANDO A API

#Criando a lista com vários alunos:
Alunos = [Aluno ("Nathan", 22, 10),
          Aluno ("Hazel", 2, 8), 
          Aluno ("Blayke", 1, 9)]

#criando um objeto para saber as notas 

media_final = calculando_media(Alunos)
print (f"A média final dos alunos é: ", media_final) 

