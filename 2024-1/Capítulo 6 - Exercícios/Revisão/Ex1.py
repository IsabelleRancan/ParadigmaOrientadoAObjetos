#Escreva uma função que recebe uma lista de números e retorna a soma de todos os elementos.
import math 

def lista_numeros(numeros):
    total = sum(numeros)
    return("A soma total dos valores da lista é: ", total)

#Testando a API

lista = [1,2,3,5,7,9]
calculando_soma = lista_numeros(lista)
print (calculando_soma)