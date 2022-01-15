tot = 0
soma = 0

cont = 0
while cont != 999:
    cont = int(input('Digite um numero [999 para parar]: '))
    if cont != 999:
        tot += 1
        soma += cont
print('Voce digitou {} numeros e a soma entre eles foi {}.'.format(tot, soma))