# 2 - Crie uma tupla de coordenadas (x, y) e calcule a distância euclidiana entre dois pontos
import math 

class Coordenadas:

    def obter_coordenadas():
        x1 = float(input("Digite a coordenada x do ponto 1: "))
        y1 = float(input("Digite a coordenada y do ponto 1: "))
        x2 = float(input("Digite a coordenada x do ponto 2: "))
        y2 = float(input("Digite a coordenada y do ponto 2: "))

        ponto1 = (x1, y1)
        ponto2 = (x2, y2)
        return ponto1, ponto2
    
    def calculando_distancia():
        return math.sqrt((ponto2[0] - ponto1[0])**2 + (ponto2[1] - ponto1[1])**2)

           
    
ponto1, ponto2 = Coordenadas.obter_coordenadas()
print("Coordenadas do ponto 1:", ponto1)
print("Coordenadas do ponto 2:", ponto2)
print("A distância entre os pontos é: ", Coordenadas.calculando_distancia())
