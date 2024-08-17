#entrada de CDs: fazer uma linha recebendo o n cds, após isso um loop com n IDs. Colocar em sets e verificar qual cd se repete com um contador

#esse map adiciona n e m que serão declarados em uma única linha 
n, m = map(int, input().split())

#criando um set para Jack
jack = set()
#adicionando cada número que o usuário vai informar dentro do set de Jack
for i in range(n):
    jack.add(int(input()))

c = 0
#criando um for para a quantidade de CDS que vão digitar para Jill
for i in range(m):
    #se o que o usuário digitar já estiver no set de Jack, ele vai adicionar mais um no contador
    #não foi necessário nem criar uma lista de jill para podermos comparar já que o programa só retorna a quantidade e n os ids do cd em si
    if int(input()) in jack:
        c += 1
print(c)
    