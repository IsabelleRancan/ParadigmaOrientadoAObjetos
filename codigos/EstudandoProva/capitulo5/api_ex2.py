import ex2

class Api:
    # Calculando o perímetro de um círculo
    def __init__(self, raio, precision):
        self.raio = raio
        self.precision = ex2.Math

    def calculo(self):
        perimetro = 2 * self.precision.pi * self.raio
        return perimetro

# Exemplo de uso com precision diferente
raio = 5.0
precision_personalizada = 3

# Criando uma instância da classe Api com precision diferente
minha_api = Api(raio=raio, precision=precision_personalizada)

# Calculando o perímetro usando a precisão personalizada
resultado_calculo = minha_api.calculo()

# Imprimindo o resultado
print(f"Perímetro do círculo com precisão {precision_personalizada}: {resultado_calculo}")
