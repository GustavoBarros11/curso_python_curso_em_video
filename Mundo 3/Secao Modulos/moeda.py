def aumentar(n=0, porc=0, fmt=False):
    porc_decimal = (porc/100)
    aumento = n * (1+porc_decimal)

    return aumento if fmt is False else moeda(aumento)

def diminuir(n=0, porc=0, fmt=False):
    porc_decimal = (porc/100)
    reducao = n * (1-porc_decimal)

    return reducao if fmt is False else moeda(reducao)

def dobro(n=0, fmt=False):
    return n*2  if fmt is False else moeda(n*2)


def metade(n=0, fmt=False):
    return n/2 if fmt is False else moeda(n/2)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, aum=10, red=5):
    print('-'*30)
    #print(f'{"RESUMO DO VALOR":^30}')
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'{"Preço analisado:":<20}{moeda(n):<10}')
    print(f'{"Dobro do preço:":<20}{moeda(dobro(n)):<10}')
    print(f'{"Metade do preço:":<20}{moeda(metade(n)):<10}')
    print(f'{aum:2}{"% de aumento:":<18}{moeda(aumentar(n, aum)):<10}')
    print(f'{red:2}{"% de redução:":<18}{moeda(diminuir(n, red)):<10}')
    print('-'*30)

