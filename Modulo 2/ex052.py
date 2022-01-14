numero = int(input('Digite um número: '))
divisores = 0

for i in range(1 , numero+1):
    if numero % i == 0:
        divisores += 1
        print('\033[1;32m{}\033[m'.format(i), end=' ')
    else:
        print('\033[1;31m{}\033[m'.format(i), end=' ')

print('\nO número {} foi divisível {} vezes\nE por isso ele '.format(numero, divisores), end='')
if divisores > 2:
    print('NÃO É PRIMO!')
else:
    print('É PRIMO!')
    