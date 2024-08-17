from collections import namedtuple

# 1 - Crie uma tupla nomeada para representar um aluno com os campos nome, idade e nota. Crie um aluno e imprima suas informações

Aluno = namedtuple("Aluno",["Nome", "Idade", "Nota"])
Alunos = [Aluno("Nathan", 24, 10), 
          Aluno("Franciele", 27, 9), 
          Aluno("Isabelle", 19, 8)] 
#se eu quiser adicionar um único aluno, basta returar os colchetes 

print(Alunos)