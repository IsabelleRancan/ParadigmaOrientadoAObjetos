#Palinagrama 

#Palindromo: palavra que é escrita da mesma forma de trás para frente ou de frente para trás
#Anagrama: palavra formada a partir de outra palavra apenas reorganizando os caracteres
#Palinagrama: é o anagrama de um palindromo (reorganização de um palindromo), 
# ou seja, palíndromo também é um palinagrama, mas o inverso nem sempre é verdade

#Entrada:O arquivo de entrada contém no máximo 6000 casos de teste. A descrição de cada caso de teste é dada abaixo.
#Cada caso consiste em uma única string S de comprimento L (1 ≤ L ≤ 500). Esta string contém apenas letras minúsculas do alfabeto inglês (‘a’ a ‘z’).
#A entrada é encerrada por uma linha contendo um único caractere cerquilha ('#'). Esta linha não precisa ser processada.

while True:
    palavra = input(str()).lower()
    if palavra == "#":
        break;
    
