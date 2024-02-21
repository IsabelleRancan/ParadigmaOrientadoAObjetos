
# 01-Criando uma classe simples
print('\n01-Criando uma classe simples ----------------------------------------------------------\n')

# Crie uma classe Python chamada Rectangle com as seguintes características:
class Rectangle:
    # A classe deve ter dois atributos: width e height, ambos inicializados como 0.
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # Implemente um método chamado set_dimensions que receba dois argumentos w e h e ajuste os atributos width e height de acordo com os valores recebidos.
    def set_dimensions(self, a, b):
        self.width = a
        self.height = b

    # Implemente um método chamado get_area que calcula e retorna a área do retângulo (área = width * height).
    def get_area(self):
        return self.width * self.height


# Desenvolva um script para testar a classe Rectangle, instanciando objetos e chamando seus métodos.
# instancia um objeto sem atributos, onde receberá os valores padrões
shapeA = Rectangle()

# instancia um objeto com atributos, onde receberá largura = 5 e altura =7
shapeB = Rectangle(5, 7)

# imprime a area de ambos objetos
print(shapeA.get_area(), shapeB.get_area())

# altera os atributos do obj shapeA, informado nova largura(2) e altura(5)
shapeA.set_dimensions(2, 5)

# imprime novamente o obj shapeA
print(shapeA.get_area())


# 02-Usando a classe Point
print('\n02-Usando a classe Point ----------------------------------------------------------------\n')

# Dada a classe Point fornecida na seção, use-a para realizar as seguintes tarefas:


class Point:
    def __init__(self, x=0, y=0):
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other_point):
        return (
            (self.x - other_point.x) ** 2
            + (self.y - other_point.y) ** 2
        ) ** (1/2)


# Crie dois objetos Point chamados point1 e point2.
point1 = Point()
point2 = Point()

# Mova point1 para a posição (5, 7) e point2 para a posição (-2, 3).
point1.move(5, 7)
point2.move(-2, 3)

# Calcule a distância entre point1 e point2 usando o método calculate_distance e imprima o resultado.
print(point1.calculate_distance(point2))

# Redefina point1 para a origem (0, 0) usando o método reset.
point1.reset()

# Calcule a distância entre point1 e point2 novamente e imprima o resultado.
print(point1.calculate_distance(point2))


# 03-Documentando uma nova classe
print('\n03-Documentando uma nova classe --------------------------------------------------------\n')

# Crie uma nova classe chamada Employee com as seguintes características:


class Employee:
    # Adicione docstrings à classe Employee e seus métodos para fornecer explicações claras de seu propósito e uso. Use docstrings de uma linha e de várias linhas para diferentes métodos.
    "Instancia um objeto que representa uma pessoa, contendo nome e salario"
    # A classe deve ter dois atributos: name (uma string) e salary (um float).

    def __init__(self, name="", salary=0):
        "seta nome e salario vazio"
        self.name = name
        self.salary = salary
    # Implemente um método chamado raise_salary que recebe um valor percentual e aumenta o salário do funcionário de acordo com esse valor.

    def raise_salary(self, percent):
        "atribui um percentyual de aumento de salario"
        self.salary = self.salary + (self.salary * (percent/100))

    # Implemente um método chamado get_info que retorna uma string contendo o nome do funcionário e o salário atual.
    def get_info(self):
        "retorna o nome da pessoa e o salario que recebe"
        return self.name + " recebe um salario de: " + str(self.salary)


# 04-Usando a classe Employee
print('\n04-Usando a classe Employee -----------------------------------------------------------\n')

# Crie dois objetos Employee com as seguintes informações:

# Funcionário 1: Nome - “John Doe”, Salário - 50000.0
# Funcionário 2: Nome - “Jane Smith”, Salário - 65000.0

personA = Employee("John Doe", 50000.0)
personB = Employee("Jane Smith", 65000.0)

# Execute as seguintes ações:

# Imprima as informações de ambos os funcionários usando o método get_info.
print(personA.get_info())
print(personB.get_info())

# Dê um aumento de 10% para os dois funcionários usando o método raise_salary.
personA.raise_salary(10)
personB.raise_salary(10)

# Imprima novamente as informações atualizadas de ambos os funcionários.
print(personA.get_info())
print(personB.get_info())


# 05-Entendendo métodos de classe
print('\n05-Entendendo métodos de classe -----------------------------------------------------------\n')

# Considere o trecho de código a seguir usando a classe Point:
p1 = Point()
p2 = Point()

p1.x = 2
p1.y = 3
p2.x = 5
p2.y = 7

distance = p1.calculate_distance(p2)
print("Distância entre p1 e p2:", distance)

# 06-Explique como o método calculate_distance funciona e como ele calcula a distância entre dois pontos. Descreva o papel do parâmetro self no método e por que ele não é passado explicitamente ao chamar o método.
print('\n06-Explique como o método calculate_distance -----------------------------------------------------------\n')

"""
Neste exemplo, foi definindo uma classe Point que representa um ponto no plano cartesiano com coordenadas (x, y).
O método calculate_distance calcula a distância entre o ponto atual (representado por self)
e outro ponto (representado por other_point), usando uma fórmula (teorema de pitagoras) entre dois pontos em um plano.

O parâmetro self desempenha o papel de referenciar o próprio objeto da classe. Quando se invoca um método em um objeto, 
o Python automaticamente passa esse objeto como o primeiro argumento, ou seja, o parâmetro self,  para o método,
isso permite que o método acesse os atributos e outros métodos do objeto.

"""
