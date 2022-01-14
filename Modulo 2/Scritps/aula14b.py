numero = 1
par = impar = 0

while numero != 0:
    numero = int(input('Digite um número ou 0 para sair: '))
    if numero != 0:
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))