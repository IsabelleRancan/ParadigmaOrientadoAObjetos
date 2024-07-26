#ex1 - combinar listas usando zip ou lançar exceção se forem de tamanhos diferentes

def combinar_listas(l1, l2):
    if len(l1) != len(l2):
        raise ValueError("As listas são de tamanhos diferentes!")
    return list(zip(l1, l2))

#teste-certo

lista1 = ["ana", "banana"]
lista2 = [1, 3]

lista_combinada = combinar_listas(lista1, lista2)
print(lista_combinada)
    
#teste-errado

lista1 = ["ana", "banana", "joana"]
lista2 = [1, 3]

lista_combinada = combinar_listas(lista1, lista2)
print(lista_combinada)

#ex2 - 