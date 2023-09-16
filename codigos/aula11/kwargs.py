def funcao(a, b, c, **kwargs):
    print(a, b, c, kwargs)
    funcao2(**kwargs)


def funcao2(d, e, f):
    print(d, e, f)


funcao(1, 2, 3, d=4, e=5, f=6)

funcao2(7, 8, 9)
