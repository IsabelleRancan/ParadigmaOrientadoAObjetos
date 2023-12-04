import ex2

math = ex2.Math()
# Exemplo de uso com precision diferente
raio = 5.0
perimetro = 2 * raio * math.pi
print('perimetro de um circulo de raio 5:', perimetro)

math.precision=2

novo_perimetro = 2 * raio * math.pi
print('perimetro de um circulo de raio 5 com menor precisão:', novo_perimetro)
