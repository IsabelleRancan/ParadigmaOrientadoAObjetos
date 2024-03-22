from dataclasses import make_dataclass

#1 - Use make_dataclass para criar uma classe para representar um ponto no espaço 3D com os campos x, y e z. 
#Crie um ponto e imprima suas coordenadas.

Ponto = make_dataclass("Ponto", [("x", float), ("y", float), ("z", float)])

#EXECUTANDO
ponto = Ponto(1.0, 2.0, 7.0)
print(f"As coordenadas do ponto são: ", ponto)