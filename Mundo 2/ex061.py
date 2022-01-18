print('Gerador de PA')
print('-='*10)
pt = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
ntermos = 10
termo = 0

contador = ntermos
while contador > 0:
    termo = pt + (10-contador) * razao
    print('{}'.format(termo), end=' -> ')
    contador -= 1
print('Fim', end='')