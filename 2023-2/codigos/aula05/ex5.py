class Point:
    "Representa um ponto em coordenadas geométricas bidimensionais."
 
    def __init__(self, x=0, y=0):
        """Inicializa a posição de um novo ponto. As coordenadas x e y
           podem ser especificadas. Se não forem, o
           ponto assume a origem."""
        self.move(x, y)
 
    def move(self, x, y):
        "Move o ponto para uma nova localização no espaço 2D."
        self.x = x
        self.y = y
 
    def reset(self):
        "Redefine o ponto para a origem geométrica: 0, 0."
        self.move(0, 0)
 
    def calculate_distance(self, other_point):
        """Calcula a distância deste ponto para um segundo
        ponto passado como parâmetro.
 
        Esta função usa o Teorema de Pitágoras para calcular
        a distância entre os dois pontos. A distância é
        retornada como um número float."""
 
        return (
            (self.x - other_point.x) ** 2
            + (self.y - other_point.y) ** 2
        ) ** (1/2)
 


p1 = Point()
p2 = Point()
 
p1.x = 2
p1.y = 3
p2.x = 5
p2.y = 7
 
distance = p1.calculate_distance(p2)
print("Distância entre p1 e p2:", distance)


"""
    O método calculate_distance calcula a distancia entre os pontos p1 e p2 utilizando o 
    Teorema de Pitágoras. Esses pontos estão em um plano cartesiano e tem as suas posições 
    definidas pelos números inseridos em x e y. 
    O "self" tem como papel fazer uma "ligação" entre o método e o objeto em questão, fazendo  
    referência aos valores dados nos atributos.  
"""
