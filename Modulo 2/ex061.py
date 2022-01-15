fatorial = int(input('Digite um numero para\ncalcular seu Fatorial: '))
resultado = 1

print('Calculando {}! = '.format(fatorial), end='')
while fatorial > 0:
    if fatorial == 1:
        print('{}'.format(fatorial), end=' ')
        fatorial -= 1
    else:
        print('{} x'.format(fatorial), end=' ')
        resultado *= fatorial
        fatorial -= 1
print('= {}'.format(resultado))