#media_valores: Recebe uma quantidade arbitrária de números como argumentos posicionais. 
# Retorna a média de todos os números passados como argumentos.

def media(*args):
    resultado = sum(args)
    resultado = resultado / len(args)
    return resultado

print(media(2,2,2))
