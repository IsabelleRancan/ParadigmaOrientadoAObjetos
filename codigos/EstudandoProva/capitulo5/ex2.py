import math

class Math:
    """Criando a classe Math e o atributo de classe precision.
    O atributo precision é o determinante do número de casas decimais após a vírgula que
    o código vai retornar."""
    precision = 5

    @property
    def pi(self):
        """Criando a propriedade de classe pi.
        Essa classe vai retornar o valor de pi com o número determinado de casas decimais."""
        formato = "{:." + str(self.precision) + "f}"  # Acessando o atributo de instância precision e definindo o formato
        return formato.format(math.pi)

# Criando uma instância da classe Math
minha_classe_math = Math()

# Acessando o método pi, formatando e imprimindo o valor
valor_formatado = minha_classe_math.pi
print("Valor de pi formatado:", valor_formatado)
teste = Math.precision(5)
print(teste)