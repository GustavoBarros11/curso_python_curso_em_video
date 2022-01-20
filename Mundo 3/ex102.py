def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcioanl) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c == 1:
                print(f'{c}', end=' = ')
            else:
                print(f'{c}', end=' x ')
    return f


print('-'*25)
# print(fatorial(5))
print(fatorial(5, show=True))
# print(fatorial(5, show=False))
# help(fatorial)