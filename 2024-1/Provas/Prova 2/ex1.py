#Implemente a função combinar_listas: Recebe duas listas. Combina os elementos das duas listas em uma lista de tuplas, 
#onde cada tupla conterá os próximos itens de cada lista. Retorna a lista de tuplas. Caso as listas sejam de tamanhos diferentes, 
#levantar uma exceção. Deve ser usada a função zip.

def combinar_listas(lista1, lista2):
    tupla = []
    c = 0

    if len(lista1) > len(lista2) or len(lista2) > len(lista1):
        print("As listas devem ter tamanhos iguais")
        
    else: 
        for i in lista1:
            tupla.append((lista1[c], lista2[c]))
            c +=1
        return (tupla)


#TESTE:
    
l1 = ["Ana", "Matheus"]
l2 = [18, 27]
lista_tuplas = combinar_listas(l1, l2)
print(lista_tuplas) 

#TESTE 2:
l1 = ["Ana", "Matheus"]
l2 = [18, 27, 35]
lista_tuplas = combinar_listas(l1, l2)
print(lista_tuplas) 