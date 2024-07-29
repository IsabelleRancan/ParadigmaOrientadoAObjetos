#entrada de CDs: fazer uma linha recebendo o n cds, após isso um loop com n IDs. Colocar em sets e verificar qual cd se repete com um contador

qntd_cd_Jack = int(input("Digite a quantidade de CDs que Jack possuí: "))
qntd_cd_Jill = int(input("Digite a quantidade de CDs que Jill possuí: "))

cd_Jack = { }
i = 0
while i < qntd_cd_Jack: 
    id = int(input("Digite o id dos CDs de Jack: "))
    cd_Jack[i] = id
    i += 1

print(cd_Jack)


cd_Jill = { }
i = 0
while i < qntd_cd_Jill: 
    id = int(input("Digite o id dos CDs de Jill: "))
    cd_Jill[i] = id
    i += 1

print(cd_Jill)

    