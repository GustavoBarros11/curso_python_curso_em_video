def fatorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


def calc(n):
    return lambda a: a * n


dobro = calc(2)
triplo = calc(3)
